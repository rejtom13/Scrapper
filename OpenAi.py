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
                    "content": f"""Twoim zadaniem jest zweryfikować opis produktu z ogłoszenia i na jego podstawie dostarczyć szczegółowe informacje o stanie urządzenia oraz ocenić zgodność modelu podanego w tytule, opisie oraz wszelkich innych wzmiankach. Użyj następujących oznaczeń przy ocenie każdej właściwości: :white_check_mark: (sprawne/brak uszkodzeń), :x: (występuje wada. Dodaj komentarz na czym polega wada), brak danych (jeśli brak informacji w opisie).

                    Kroki do wykonania:
                    **Oceń stan urządzenia**: Na podstawie dostępnych informacji dokonaj oceny poszczególnych cech wymienionych poniżej.
                    
                    Poniżej zweryfikuj te elementy dla urządzenia i zwróc tylko tę listę poniżej jako szablon wiadomosci.:
                    
                    **Model**: **  
                    **Wyświetlacz**: **  
                    **Tył**: **  
                    **Aparat przód/tył**: **  
                    **FaceID**: **  
                    **Wifi/Bluetooth/Sieć komórkowa**: **  
                    **Blokada**: **  
                    **Pudełko**: **  
                    **Kondycja baterii**: (podaj tylko procent, jeśli jest dostępny) %  
                    **Inne wady**: **  
                    
                    Opis do weryfikacji: {description}
                    Tytuł do weryfikacji: {title}
                    Model do weryfikacji: {model}
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
                :x: (jeśli występuje wada + dodaj komentarz (koniecznie po polsku) na czym polega wada)
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
