from contextlib import suppress

import httpx
import pytest
from decouple import UndefinedValueError, config
from tenacity import retry, retry_if_exception, wait_random_exponential

retryable_status_codes = (
    httpx.codes.TOO_MANY_REQUESTS,
    httpx.codes.INTERNAL_SERVER_ERROR,
    httpx.codes.BAD_GATEWAY,
    httpx.codes.SERVICE_UNAVAILABLE,
    httpx.codes.GATEWAY_TIMEOUT,
)


def retry_predicate(exception):
    """Return whether to retry. This depends on getting an exception with a response
    object, and that response object having one of the status codes that we can retry.
    """
    return (
        hasattr(exception, "response")
        and exception.response.status_code in retryable_status_codes
    )


@pytest.fixture(scope="session")
def clerk_secret_key(request):
    """Retrieve the clerk secret key to use for the test.

    If using AWS Secrets Manager, the CLERK_SECRET_ID variable be set to the ID of the
    SecretsManager secret that contains the Clerk secret key. This can be set in a .env
    file or an environment variable.

    If not using AWS Secrets Manager, the CLERK_SECRET_KEY variable must be set to the
    value of the clerk secret key to use. This can be set in a .env file or an
    environment variable.
    """
    with suppress(UndefinedValueError, pytest.FixtureLookupError):
        secretsmanager_client = request.getfixturevalue("secretsmanager_client")
        return secretsmanager_client.get_secret_value(
            SecretId=config("CLERK_SECRET_ID")
        )["SecretString"]

    with suppress(UndefinedValueError):
        return config("CLERK_SECRET_KEY")

    pytest.skip(
        reason="Neither CLERK_SECRET_ID nor CLERK_SECRET_KEY was found in the"
        " environment or a .env file and is required for this test. If CLERK_SECRET_ID"
        " is set, and you're still seeing this message, ensure the aws extra"
        " dependencies are installed."
    )


@pytest.fixture(scope="session")
def clerk_backend_httpx_client(clerk_secret_key):
    """A fixture that creates a HTTPX Client instance with the required backend Clerk
    Authorization headers set and the correct Clerk backend API base URL.

    Please be mindful of the Clerk API rate limits:
    https://clerk.com/docs/reference/rate-limits
    """
    client = httpx.Client(
        headers={"Authorization": f"Bearer {clerk_secret_key}"},
        base_url="https://api.clerk.com/v1",
    )

    yield client

    client.close()


@pytest.fixture(scope="session")
def clerk_frontend_api_url():
    """This fixture returns the value of the CLERK_FRONTEND_URL variable and is used to
    make calls to the Clerk frontend API.

    CLERK_FRONTEND_URL can be set via environment variables or in a .env file. This URL
    can be found under Developers -> API Keys -> Show API URLs.
    """
    with suppress(UndefinedValueError):
        return config("CLERK_FRONTEND_URL")

    pytest.skip(
        reason="CLERK_FRONTEND_URL was not found in the environment or a .env file and"
        " is required for this test."
    )


@pytest.fixture(scope="session")
def clerk_frontend_httpx_client(clerk_frontend_api_url):
    """This fixture returns a function that creates an HTTPX Client instance with the
    required frontend Clerk Authorization parameters set and the correct Clerk frontend
    API base URL.

    This requires the CLERK_FRONTEND_URL variable to be set. CLERK_FRONTEND_URL can be
    set via environment variables or in a .env file. This URL can be found under
    Developers -> API Keys -> Show API URLs.
    """
    with httpx.Client(base_url=f"{clerk_frontend_api_url}/v1") as client:
        result = client.post(url="/dev_browser")

    result.raise_for_status()

    client = httpx.Client(
        params={"__dev_session": result.json()["token"]},
        base_url=f"{clerk_frontend_api_url}/v1",
    )

    yield client

    client.close()


@pytest.fixture
def clerk_delete_org(clerk_backend_httpx_client):
    """This fixture provides a function to delete an organization given an org ID. Any
    additional kwargs are passed through to the httpx.Client.delete call.

    The API documentation for this call can be found below:
    https://clerk.com/docs/reference/backend-api/tag/Organizations#operation/DeleteOrganization
    """

    @retry(
        retry=retry_if_exception(predicate=retry_predicate),
        wait=wait_random_exponential(multiplier=0.5, max=60),
    )
    def _inner(org_id, **kwargs):
        """Delete the org with the given org ID. Any additional kwargs are passed
        through to the httpx.Client.delete call.

        This will retry rate limit errors.

        The API documentation for this call can be found below:
        https://clerk.com/docs/reference/backend-api/tag/Organizations#operation/DeleteOrganization
        """
        return clerk_backend_httpx_client.delete(
            url=f"/organizations/{org_id}", **kwargs
        )

    return _inner


@pytest.fixture
def clerk_create_org(clerk_backend_httpx_client, clerk_delete_org):
    """This fixture provides a function to create an organization that will
    automatically be deleted on fixture teardown.

    The API documentation for this call can be found below:
    https://clerk.com/docs/reference/backend-api/tag/Organizations#operation/CreateOrganization
    """
    orgs_to_delete = []

    @retry(
        retry=retry_if_exception(predicate=retry_predicate),
        wait=wait_random_exponential(multiplier=0.5, max=60),
    )
    def _inner(organization_data, **kwargs):
        """This function creates an Organization with the provided organization_data,
        and saves the reference to delete it at a later time. All additional kwargs are
        passed through to the httpx.Client.post call.

        This will retry rate limit errors.

        The API documentation for this call can be found below:
        https://clerk.com/docs/reference/backend-api/tag/Organizations#operation/CreateOrganization
        """
        nonlocal orgs_to_delete

        result = clerk_backend_httpx_client.post(
            url="/organizations", json=organization_data, **kwargs
        )
        result.raise_for_status()
        result = result.json()
        orgs_to_delete.append(result)
        return result

    yield _inner

    # Now remove all of the orgs.
    for org in orgs_to_delete:
        clerk_delete_org(org_id=org["id"])


@pytest.fixture
def clerk_get_org(clerk_backend_httpx_client):
    """This fixture provides a function to get an organization by its ID or slug. All
    additional kwargs are passed through to the httpx.Client.get call.

    The API documentation for this call can be found below:
    https://clerk.com/docs/reference/backend-api/tag/Organizations#operation/GetOrganization
    """

    @retry(
        retry=retry_if_exception(predicate=retry_predicate),
        wait=wait_random_exponential(multiplier=0.5, max=60),
    )
    def _inner(org_id_or_slug, **kwargs):
        """This function attempts to find and return the org with the given ID or slug.
        All additional kwargs are passed through to the httpx.Client.get call.

        This will retry rate limit errors.

        The API documentation for this call can be found below:
        https://clerk.com/docs/reference/backend-api/tag/Organizations#operation/GetOrganization
        """
        result = clerk_backend_httpx_client.get(
            url=f"/organizations/{org_id_or_slug}", **kwargs
        )
        result.raise_for_status()
        return result.json()

    yield _inner


@pytest.fixture
def clerk_delete_user(clerk_backend_httpx_client):
    """This fixture provides a function to delete a user given the user ID. All
    additional kwargs are passed through to the httpx.Client.delete call.

    The API documentation for this call can be found below:
    https://clerk.com/docs/reference/backend-api/tag/Users#operation/DeleteUser
    """

    @retry(
        retry=retry_if_exception(predicate=retry_predicate),
        wait=wait_random_exponential(multiplier=0.5, max=60),
    )
    def _inner(user_id, **kwargs):
        """Delete the user with the given user ID. All additional kwargs are passed
        through to the httpx.Client.delete call.

        This will retry rate limit errors.

        The API documentation for this call can be found below:
        https://clerk.com/docs/reference/backend-api/tag/Users#operation/DeleteUser
        """
        return clerk_backend_httpx_client.delete(url=f"/users/{user_id}", **kwargs)

    return _inner


@pytest.fixture
def clerk_create_user(clerk_backend_httpx_client, clerk_delete_user):
    """This fixture provides a method to create a user that will automatically
    be deleted on fixture teardown.

    The API documentation for this call can be found below:
    https://clerk.com/docs/reference/backend-api/tag/Users#operation/CreateUser
    """
    users_to_delete = []

    @retry(
        retry=retry_if_exception(predicate=retry_predicate),
        wait=wait_random_exponential(multiplier=0.5, max=60),
    )
    def _inner(user_data, **kwargs):
        """This function uses user_data to create a User with the backend API, and
        saves the reference to delete it at a later time. All other kwargs are passed
        through to the httpx.Client.post call.

        This will retry rate limit errors.

        The API documentation for this call can be found below:
        https://clerk.com/docs/reference/backend-api/tag/Users#operation/CreateUser
        """
        nonlocal users_to_delete
        result = clerk_backend_httpx_client.post(url="/users", json=user_data, **kwargs)
        result.raise_for_status()
        result = result.json()
        users_to_delete.append(result)
        return result

    yield _inner

    # Now remove all of the users.
    for user in users_to_delete:
        clerk_delete_user(user_id=user["id"])


@pytest.fixture
def clerk_add_org_member(clerk_backend_httpx_client):
    """This fixture provides a function to add a user to an organization. All additional
    kwargs are passed through to the httpx.Client.post call.

    The API documentation for this call can be found below:
    https://clerk.com/docs/reference/backend-api/tag/Organization-Memberships#operation/CreateOrganizationMembership
    """

    @retry(
        retry=retry_if_exception(predicate=retry_predicate),
        wait=wait_random_exponential(multiplier=0.5, max=60),
    )
    def _inner(org_id, user_id, role, **kwargs):
        """Add's the provided user ID to the provided org ID with the provided role. All
        additional kwargs are passed through to the httpx.Client.post call.

        This will retry rate limit errors.

        The API documentation for this call can be found below:
        https://clerk.com/docs/reference/backend-api/tag/Organization-Memberships#operation/CreateOrganizationMembership
        """
        result = clerk_backend_httpx_client.post(
            url=f"/organizations/{org_id}/memberships",
            json={"user_id": user_id, "role": role},
            **kwargs,
        )
        result.raise_for_status()
        return result.json()

    return _inner


@pytest.fixture
def clerk_sign_user_in(clerk_frontend_httpx_client):
    """This fixture returns a function that, given a Clerk User's email and password,
    will sign that user in and return the resulting sign in object from the front end
    API. All additional kwargs are passed through to the httpx.Client.post call.

    The API documentation for this call can be found below:
    https://clerk.com/docs/reference/frontend-api/tag/Sign-Ins#operation/createSignIn
    """

    @retry(
        retry=retry_if_exception(predicate=retry_predicate),
        wait=wait_random_exponential(multiplier=0.5, max=60),
    )
    def _inner(email, password, **kwargs):
        """Attempts to sign in the user using the provided email and password, and then
        returns the sign in object. All additional kwargs are passed through to the
        httpx.Client.post call.

        This will retry rate limit errors.

        The API documentation for this call can be found below:
        https://clerk.com/docs/reference/frontend-api/tag/Sign-Ins#operation/createSignIn
        """
        result = clerk_frontend_httpx_client.post(
            url="/client/sign_ins",
            data={"strategy": "password", "identifier": email, "password": password},
            **kwargs,
        )
        result.raise_for_status()
        result = result.json()
        assert result["response"]["status"] == "complete"
        return result

    return _inner


@pytest.fixture
def clerk_touch_user_session(clerk_frontend_httpx_client):
    """This fixture returns a function that, given a Clerk user session ID and any
    optional session_data, touch the session with the given ID with any session_data
    sent as form data. This passes through any additional kwargs to the
    httpx.Client.post call.

    The API documentation for this call can be found below:
    https://clerk.com/docs/reference/frontend-api/tag/Sessions#operation/touchSession
    """

    @retry(
        retry=retry_if_exception(predicate=retry_predicate),
        wait=wait_random_exponential(multiplier=0.5, max=60),
    )
    def _inner(session_id, session_data=None, **kwargs):
        """Given a Clerk user session ID and any optional session_data, touch the
        session with the given ID with any session_data sent as form data. This passes
        through any additional kwargs to the httpx.Client.post call.

        This will retry rate limit errors.

        The API documentation for this call can be found below:
        https://clerk.com/docs/reference/frontend-api/tag/Sessions#operation/touchSession
        """
        result = clerk_frontend_httpx_client.post(
            url=f"/client/sessions/{session_id}/touch", data=session_data, **kwargs
        )
        result.raise_for_status()
        return result.json()

    return _inner


@pytest.fixture
def clerk_set_user_active_org(clerk_touch_user_session):
    """This fixture returns a function that, given a Clerk user session ID and an
    organization ID, attempts to set that organization as active.

    The user must already be a member of the organization for this to work.

    Any additional kwargs are passed through to the httpx.Client.post call.
    """

    def _inner(session_id, org_id, **kwargs):
        """Given a Clerk user session ID and an organization ID, this function attempts
        to set that organization as active.

        The user must already be a member of the organization for this to work.

        Any additional kwargs are passed through to the httpx.Client.post call.
        """
        return clerk_touch_user_session(
            session_id=session_id,
            session_data={"active_organization_id": org_id},
            **kwargs,
        )

    return _inner


@pytest.fixture
def clerk_get_user_session_token(clerk_frontend_httpx_client):
    """This fixture returns a function that, given a Clerk session ID, will retrieve a
    currently valid session token for the user tied to that session.

    Any additional kwargs are passed through to the httpx.Client.post call.

    The API documentation for this call can be found below:
    https://clerk.com/docs/reference/frontend-api/tag/Sessions#operation/createSessionToken
    """

    @retry(
        retry=retry_if_exception(predicate=retry_predicate),
        wait=wait_random_exponential(multiplier=0.5, max=60),
    )
    def _inner(session_id, **kwargs):
        """Retrieves a currently valid session token for the user tied to the provided
        session ID.

        Any additional kwargs are passed through to the httpx.Client.post call.

        This will retry rate limit errors.

        The API documentation for this call can be found below:
        https://clerk.com/docs/reference/frontend-api/tag/Sessions#operation/createSessionToken
        """
        result = clerk_frontend_httpx_client.post(
            url=f"/client/sessions/{session_id}/tokens", **kwargs
        )
        result.raise_for_status()
        return result.json()["jwt"]

    return _inner
