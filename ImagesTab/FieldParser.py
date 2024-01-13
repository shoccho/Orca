from datetime import datetime

def parse_images_data(data):
    result = []
    for (key, value) in data:
        if key == 'Created':
            dt_object = datetime.fromtimestamp(value)
            result.append(dt_object.strftime('%H:%M %d/%m/%Y'))
        elif key == 'Id':
            id = value.split(':')[1][0:6]
            result.append(id)
        elif key == "RepoDigests":
            continue
        elif key.endswith('Size'):
            size = int(value)/(1000_000)
            result.append(f'{size} Mb')
        else:
            result.append(str(value))
    return result