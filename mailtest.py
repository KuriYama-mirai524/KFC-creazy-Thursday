import pandas as pd


# 标签映射关系
label_mapping = {
    '邮件号': '邮件号',
    '*寄件人姓名': '寄件人姓名',
    '*寄件人电话/手机': '寄件人手机号',
    '*寄件人地址': '寄件人详细地址',
    '*收件人姓名': '收件人姓名',
    '*收件人电话/手机': '收件人手机号',
    '*收件人地址': '收件人详细地址'
}

# 固定的字段值
fixed_values = {
    '重量': 100,
    '内件性质': 1,
    '运输方式': 1,
    '商品名称': 2
}

# 读取原始excel表格数据
excel_file = input("输入表格：")
try:
    original_data = pd.read_excel(excel_file)
except Exception as e:
    # 如果读取失败，尝试使用 xlrd 引擎读取 .xls 文件
    original_data = pd.read_excel(excel_file, engine='xlrd')

# 创建空的新数据表格
new_data = pd.DataFrame(columns=['邮件号', '内件号', '寄件人姓名', '寄件人手机号', '寄件人详细地址', '收件人姓名', '收件人手机号', '收件人详细地址', '重量', '内件性质', '运输方式', '商品名称'])

# 循环查询邮件号
while True:
    # 输入待查询的邮件号或输入q退出
    mail_number = input("请输入邮件号(输入q退出)：")
    if mail_number.lower() == 'q':
        break

    # 检查是否已存在相同的邮件号
    if mail_number in new_data['邮件号'].values:
        print(f"邮件号 {mail_number} 已存在，忽略该次输入")
        continue

    # 根据邮件号匹配对应的行
    matched_row = original_data[original_data['邮件号'] == int(mail_number)]

    # 检查是否有匹配的行
    if len(matched_row) > 0:
        # 提取所需的字段并按新数据标签进行重命名
        row_data = matched_row[list(label_mapping.keys())].copy()
        row_data.rename(columns=label_mapping, inplace=True)

        # 处理收件人手机号
        if '*' in row_data['收件人手机号']:
            row_data['收件人手机号'] = row_data['收件人手机号'].str.split('/').str[0]

        # 添加固定字段值
        for column, value in fixed_values.items():
            row_data[column] = value

        # 将匹配的行添加到新数据表格
        new_data = pd.concat([new_data, row_data], ignore_index=True)
    else:
        print("未找到邮件号对应的数据")

# 生成新的excel表格文件名
sender_name = new_data['寄件人姓名'].iloc[0]
output_file = f"{sender_name}.xlsx"

# 保存新的excel表格数据
while True:
    try:
        new_data.to_excel(output_file, index=False)
        break
    except PermissionError:
        print(f"无法保存表格文件，请关闭已打开的文件: {output_file}")
        input("按任意键继续...")
        continue

print(f"生成新的excel表格成功: {output_file}")
