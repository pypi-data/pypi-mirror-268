from keycloak import KeycloakOpenID

class IdentityProvider:
    def __init__(self, client_id, client_secret, realm, idp_url, logger, username=None, password=None):
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__realm = realm
        self.__idp_url = idp_url

        self.__connection = None
        self.__token_set = None
        self.__access_token = None
        self.__refresh_token = None
        self.__logger = logger
        self.__username = username
        self.__password = password

    @property
    def client_id(self):
        return self.__client_id

    @property
    def token_set(self):
        return self.__token_set

    @property
    def access_token(self):
        return self.__access_token

    @property
    def refresh_token(self):
        return self.__refresh_token

    def connect(self):
        self.__logger.info("Connect to the Identity Provider")
        self.__connection = KeycloakOpenID(
            server_url=self.__idp_url,
            realm_name=self.__realm,
            client_id=self.__client_id,
            client_secret_key=self.__client_secret
        )

    def get_token_set(self):
        if self.__username and self.__password:
            self.__token_set = self.__connection.token(
                username=self.__username,
                password=self.__password
            )
        else:
            self.__token_set = self.__connection.token(
                grant_type=["client_credentials"]
            )
        if self.__token_set:
            self.__logger.info("Token set obtained")
            self.__access_token = self.__token_set["access_token"]
            self.__refresh_token = self.__token_set["refresh_token"]

    def refresh_token_set(self):
        if self.__refresh_token:
            __token_set = self.__connection.refresh_token(
                self.__refresh_token
            )
            if __token_set["refresh_token"] != self.__token_set["refresh_token"] and __token_set["access_token"] != self.__token_set["access_token"]:
                self.__logger.info("Token set refreshed")
                self.__token_set = __token_set
                if self.__token_set:
                    self.__access_token = self.__token_set["access_token"]
                    self.__refresh_token = self.__token_set["refresh_token"]
