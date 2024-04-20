class StiLicenseStatic:

### Private

    __licenseKey: str = None
    __licenseFile: str = None

### Static

    @staticmethod
    def setKey(key: str) -> None:
        """Set the license key in Base64 format."""

        StiLicenseStatic.__licenseKey = key

    @staticmethod
    def setFile(file: str) -> None:
        """Set the path or URL to the license key file."""

        StiLicenseStatic.__licenseFile = file
        