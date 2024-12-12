from datetime import datetime
from django.core.exceptions import ValidationError


def validate_robot_data(data):
    try:
        model = data.get('model')
        version = data.get('version')
        created_str = data.get('created')

        if not model or not version or not created_str:
            raise ValidationError("Все поля 'model', 'version' и 'created' обязательны.")

        created = datetime.strptime(created_str, '%Y-%m-%d %H:%M:%S')

        if not isinstance(model, str) or not isinstance(version, str):
            raise ValidationError("Модель и версия должны быть строками.")

        serial = f"{model}-{version}"

        return {'model': model, 'version': version, 'created': created, 'serial': serial}
    except Exception as e:
        raise ValidationError(f"Ошибка в данных: {str(e)}")
