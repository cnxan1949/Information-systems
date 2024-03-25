import pandas as pd

# 加载CSV文件
csv_file = 'C:\\Users\\韩韩\\Desktop\\毕业设计\\代码\\file_list.csv'
data = pd.read_csv(csv_file, encoding='GBK')

# 中文到俄语的翻译字典
translation_dict = {
    '数据重复性检测：': 'Проверка на дублирование данных:',
    '数据中存在重复行：': 'Дубликаты присутствуют в данных:',
    '数据中不存在重复行。': 'Дубликаты отсутствуют в данных.',
    '数据缺失性检测：': 'Проверка на пропущенные данные:',
    '数据中存在缺失行：': 'Пропущенные данные присутствуют в данных:',
    '数据中不存在缺失行。': 'Пропущенные данные отсутствуют в данных.',
    '数据类型检测：': 'Проверка типов данных:'
}

# 步骤1：数据重复性检测
print(translation_dict['数据重复性检测：'])
duplicate_rows = data[data.duplicated()]
if not duplicate_rows.empty:
    print(translation_dict['数据中存在重复行：'])
    print(duplicate_rows)
else:
    print(translation_dict['数据中不存在重复行。'])

# 步骤2：数据缺失性检测
print("\n" + translation_dict['数据缺失性检测：'])
missing_data = data.isnull().sum()
if missing_data.any():
    print(translation_dict['数据中存在缺失行：'])
    print(missing_data)
else:
    print(translation_dict['数据中不存在缺失行。'])

# 步骤3：数据类型检测
print("\n" + translation_dict['数据类型检测：'])
print(data.dtypes)

