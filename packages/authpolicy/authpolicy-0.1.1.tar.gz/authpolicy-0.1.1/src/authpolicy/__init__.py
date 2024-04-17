from authpolicy import config
from authpolicy.src.PermissionsClass import PermissionsClass

__version__ = config.SDK_VERSION


class AuthPolicy:
    def __init__(self, pdp: str, client_id: str):
        self.pdp = pdp
        self.client_id = client_id
        self.__validate_credentials()

    def __pdp_validation(self, url):
        if not (url and type(url)):
            raise ValueError(f'Invalid PDP provided. Please make sure the PDP address "{self.pdp}" is correct.')

        if not (url[:7] == 'http://' or url[:8] == 'https://'):
            raise ValueError('PDP URL should be fully qualified URL with HTTP scheme.')

        domain = url.split('//')[-1].split(':')[0]
        if domain not in ('localhost', '127.0.0.1'):
            raise ValueError('PDP domain should be a localhost for optimal performance.')

    def __validate_credentials(self):
        self.__pdp_validation(self.pdp)

        if not (self.client_id and type(self.client_id) is str):
            raise ValueError(f'Invalid Client ID. Please make sure a correct Client ID is provided.')

    def is_allowed(self, member_uid: str, resource_name: str, operation: str = 'read'):
        """
        Checks if a user is allowed to perform an operation on a given resource.
        Operation can be Read/Create/Update/Delete.

        Args:
            member_uid: The unique ID for the user that you have synced with AuthPolicy.com.
            resource_name: The name of the resource you have created on AuthPolicy.com.
            operation: The operation that's being performed E.g. Read/Create/Update/Delete. Defaults to Read.

        Returns:
            True: Indicates that the user is authorized for the resource and the operation being performed.
            False: Indicates that the user is not authorized for the resource and the operation being performed.
            None: Indicates the data was not found to make the decision for the user.

        Raises:
            ValueError: In the vent of an error occurring while sending the request to the PDP.

        Examples:
            await auth_policy.is_allowed(member_uid='myUser@domainName.com',
                                        resource_name='Reports',
                                        operation='create')
        """

        permissions_class = PermissionsClass(pdp=self.pdp, client_id=self.client_id)
        return permissions_class.make_request_to_pdp(member_uid=member_uid,
                                                     resource_name=resource_name,
                                                     operation=operation)
