from datetime import date

from django import forms


class TourForm(forms.Form):
    destination = forms.ChoiceField(
        label="Куда едем?",
        choices=[
            ("turkey", "Турция"),
            ("thailand", "Таиланд"),
            ("uae", "ОАЭ"),
            ("russia", "Сочи, Россия"),
        ],
    )
    departure = forms.ChoiceField(
        label="Город вылета",
        choices=[
            ("ekb", "Екатеринбург"),
            ("msk", "Москва"),
            ("spb", "Санкт-Петербург"),
        ],
    )
    departure_date = forms.DateField(
        label="Дата вылета",
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(attrs={"type": "date", "min": date.today().isoformat()}),
    )
    nights = forms.IntegerField(label="Ночей", min_value=1, max_value=30, initial=7)
    adults = forms.IntegerField(label="Взрослых", min_value=1, max_value=12, initial=2)
    children = forms.IntegerField(label="Детей", min_value=0, max_value=12, initial=0)
    hotel = forms.ChoiceField(
        label="Категория отеля",
        choices=[("3", "3 звезды"), ("4", "4 звезды"), ("5", "5 звёзд")],
        initial="4",
    )
    meal = forms.ChoiceField(
        label="Питание",
        choices=[
            ("breakfast", "Завтраки"),
            ("half", "Завтрак и ужин"),
            ("all", "Всё включено"),
        ],
        initial="breakfast",
    )
    transfer = forms.BooleanField(label="Трансфер из аэропорта", required=False, initial=True)
    insurance = forms.BooleanField(label="Страховка", required=False, initial=True)

    def clean_departure_date(self):
        value = self.cleaned_data["departure_date"]
        if value < date.today():
            raise forms.ValidationError("Дата вылета не может быть в прошлом.")
        return value
