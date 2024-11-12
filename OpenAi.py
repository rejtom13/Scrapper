from openai import OpenAI

class OpenAIAgent:
    def __init__(self):
        self.client = OpenAI()

    def rate_ad(self, description):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Jesteś doradcą zakupowym i Twoim zadaniem jest analizowanie opisu produktu "},
                {
                    "role": "user",
                    "content": f"""Twoim zadaniem jest zweryfikować opis produktu z ogłoszenia i na jego podstawie określić czy jest informacja o uszkodzonym ekranie, uszkodzonym tyle telefonu, uszkodzonym wifi/bluetooth/odczycie sieci komórkowej/, faceid, uszkodzonym aparcie, czy nie jest zablokowany, jaka jest kondycja ( w domyśle baterii) lub czy są jakieś inne informacje o wadach. Poniżej opis który należy zweryfikować: 
                    {description}
                    Odpowiedź podaj w postaci bez wstępu i podsumowania, skorzystaj z (takich opcji: 
                        :white_check_mark: (jeśli dana cecha jest sprawna/brak uszkodzeń)
                        :x: (jeśli występuje wada + dodaj komenatrz na czym polega wada)
                        brak danych (jeśli brak informacji w opisie): 
                    **Wyświetlacz**</b>: 
                    **Tył**: 
                    **Apart przód**: 
                    **Apart tył**: 
                    **FaceID**: 
                    **Wifi/Bluetooth/Sieć komórkowa**:
                    **Blokada**: 
                    **Pudełko**: 
                    **Kondycja baterii**: (podaj tylko liczbę jeśli jest) %
                    **Inne wady**: 
                """

                }
            ]
        )
        return completion.choices[0].message.content