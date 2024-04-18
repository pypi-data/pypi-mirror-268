class VolumeRequest:
    create_if_not_exists: bool = False
    optional: bool = False
    name: str

    def __init__(self, name: str, create_if_not_exists: bool = None, optional: bool = None):
        self.name = name
        self.create_if_not_exists = create_if_not_exists or None
        self.optional = optional or False
