from typing import Any, Dict

from Listing import Listing


class CarListing(Listing):
    """Reprezentuje ogłoszenie samochodu z dodatkowymi szczegółami."""

    def __init__(self, data: Dict[str, Any]) -> None:
        super().__init__(data)
        params = data.get('params', [])
        params_dict = {param['key']: param.get('normalizedValue', param.get('value', '')) for param in params}

        self.vin: str = params_dict.get('vin', '')
        self.model: str = params_dict.get('model', '')
        self.year: str = params_dict.get('year', '')
        self.petrol: str = params_dict.get('petrol', '')
        self.car_body: str = params_dict.get('car_body', '')
        self.mileage: str = params_dict.get('milage', '')
        self.color: str = params_dict.get('color', '')
        self.engine_size: str = params_dict.get('enginesize', '')
        self.condition: str = params_dict.get('condition', '')
        self.transmission: str = params_dict.get('transmission', '')
        self.country_origin: str = params_dict.get('country_origin', '')
        self.engine_power: str = params_dict.get('enginepower', '')
        self.drive: str = params_dict.get('drive', '')