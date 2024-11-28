from openai import OpenAI

class OpenAIAgent:
    def __init__(self):
        self.client = OpenAI()

    def rate_ad_without_photo(self, description, model, title):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Jesteś doradcą zakupowym i Twoim zadaniem jest analizowanie opisu produktu "},
                {
                    "role": "user",
                    "content": f"""Twoim zadaniem jest zweryfikować opis produktu z ogłoszenia i na jego podstawie określić 
                    czy jest informacja o uszkodzonym ekranie, uszkodzonym tyle telefonu, 
                    uszkodzonym wifi/bluetooth/odczycie sieci komórkowej/, faceid, uszkodzonym aparcie, 
                    czy nie jest zablokowany, jaka jest kondycja/pojemność ( w domyśle baterii) lub czy są jakieś inne informacje 
                    o wadach oraz na podstawie opisu i tytyłu {title} porównać z modelem {model} i zrócić niformację 
                    czy model jest poprawny. Poniżej opis który należy zweryfikować: 
                    {description},
                    Odpowiedź podaj języku polskim w postaci bez wstępu i podsumowania, skorzystaj z (takich opcji: 
                        :white_check_mark: (jeśli dana cecha jest sprawna/brak uszkodzeń)
                        :x: (jeśli występuje wada + dodaj komenatrz na czym polega wada)
                        brak danych (jeśli brak informacji w opisie): 
                    **\nModel**: 
                    **\nWyświetlacz**: 
                    **\nTył**: 
                    **\nApart przód/tył**: 
                    **\nFaceID**: 
                    **\nWifi/Bluetooth/Sieć komórkowa**:
                    **\nBlokada**: 
                    **\nPudełko**: 
                    **\nKondycja baterii**: (podaj tylko liczbę jeśli jest) %
                    **\nInne wady**: 
                """
                }
            ]
        )
        return completion.choices[0].message.content

    def rate_ad(self, description, model, title, images):
        image_messages = [{"type": "image_url", "image_url": {"url": image}} for image in images]

        # Główna wiadomość użytkownika z opisem
        main_message = {
            "type": "text",
            "text": f"""Twoim zadaniem jest zweryfikować opis produktu z ogłoszenia i załączone zdjęcia i na tej
            podstawie określić czy jest informacja o uszkodzonym ekranie(pęknięcia/zarysowania), 
            uszkodzonym tyle telefonu (pęknięcia/zarysowania), uszkodzonym wifi/bluetooth/odczycie sieci komórkowej/, faceid, uszkodzonym aparacie, 
            czy nie jest zablokowany, jaka jest kondycja ( w domyśle baterii) lub czy są jakieś inne informacje 
            o wadach oraz na podstawie opisu i tytułu {title} porównać z modelem {model} i zwrócić informację 
            czy model jest poprawny. Poniżej opis, który należy zweryfikować: 
            {description},
            Odpowiedź podaj języku polskim w postaci bez wstępu i podsumowania, skorzystaj z (takich opcji: 
                :white_check_mark: (jeśli dana cecha jest sprawna/brak uszkodzeń)
                :x: (jeśli występuje wada + dodaj komentarz na czym polega wada)
                brak danych (jeśli brak informacji w opisie): 
            **\nModel**: 
            **\nWyświetlacz**: 
            **\nTył**: 
            **\nApart przód/tył**: 
            **\nFaceID**: 
            **\nWifi/Bluetooth/Sieć komórkowa**:
            **\nBlokada**: 
            **\nPudełko**: 
            **\nKondycja baterii**: (podaj tylko liczbę jeśli jest) %
            **\nInne wady**: 
        """
        }

        # Tworzenie listy wiadomości
        messages = [
            {"role": "system",
             "content": "Jesteś doradcą zakupowym i Twoim zadaniem jest analizowanie opisu produktu "},
            {"role": "user", "content": image_messages + [main_message]}
        ]

        # Wysłanie zapytania do modelu
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        # Zwracanie odpowiedzi
        return completion.choices[0].message.content
