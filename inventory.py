from item import Consumable, item_from_dict

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if isinstance(item, Consumable):
            matching_items = self.find_all_by_template(template_id= item.template_id)
            if matching_items:
                matching_items[0].quantity += item.quantity
                return
            else:
                self.items.append(item)
                return
        
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    @classmethod
    def from_list(cls, data_list):
        inventory = cls()
        for data in data_list:
            inventory.items.append(item_from_dict(item= data))
        return inventory

    def to_list(self):
        data = []
        for item in self.items:
            data.append(item.to_dict())
        return data
    
    def find_all_by_template(self, template_id : str):
        return [item for item in self.items if item.template_id == template_id]