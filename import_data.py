import pymxs
import openpyxl


# Блок импорта данных из 3d Max
rt = pymxs.runtime
objects = rt.objects
data_list: list[dict] = []

for obj in objects:
    if rt.isKindOf(obj, rt.GeometryClass):
        obj_name: str = obj.name

        obj_data: dict[str, float | str] = {
            "name": obj_name,
            "x_bbox": obj.max.x - obj.min.x,
            "y_bbox": obj.max.y - obj.min.y,
            "z_bbox": obj.max.z - obj.min.z
        }

        data_list.append(obj_data)


# Блок записи данных в Excel файл. (для более сложных задач можно вынести в отдельный модуль и доработать)
workbook = openpyxl.Workbook()
worksheet = workbook.active

worksheet.append(["Object name", "X bbox", "Y bbox", "Z bbox"])
for data in data_list:
    worksheet.append([data["name"], data['x_bbox'], data['y_bbox'], data['z_bbox']])

path: str = 'C:/Users/Professional/Desktop/orlov_dmitrii_tt.xlsx'
# Замените в path название файла на необходимое и путь к месту, где нужно создать Excel файл.
workbook.save(path)
