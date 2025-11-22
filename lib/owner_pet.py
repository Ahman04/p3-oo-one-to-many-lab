class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return all pets that belong to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign a pet to this owner, validating Pet type."""
        if not isinstance(pet, Pet):
            raise Exception("Must add a Pet instance")

        pet.owner = self

    def get_sorted_pets(self):
        """Return the owner's pets sorted by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet_type")
        self.pet_type = pet_type

        # Validate owner if provided
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be Owner instance")

        self.owner = owner

        # Add to class-level all list
        Pet.all.append(self)
