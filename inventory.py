from item import Consumable, item_from_dict

class Inventory:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        if isinstance(item, Consumable):
            matching_items = self.find_all_by_template(template_id= item.template_id)
            if matching_items:
                matching_items[0].quantity += item.quantity
                return
            else:
                self._items.append(item)
                return
        
        self._items.append(item)

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
    
    @property
    def items(self):
        return list(self._items)

    @classmethod
    def from_list(cls, data_list):
        inventory = cls()
        for data in data_list:
            item = item_from_dict(item= data)
            if item:
                inventory._items.append(item)
        return inventory

    def to_list(self):
        data = []
        for item in self.items:
            data.append(item.to_dict())
        return data
    
    def find_all_by_template(self, template_id : str):
        return [item for item in self.items if getattr(item, 'template_id', None) == template_id]