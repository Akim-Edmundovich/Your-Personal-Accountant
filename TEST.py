input_file = "datadump.json"
output_file = "datadump_utf8.json"

with open(input_file, "r", encoding="utf-16") as f:
    data = f.read()

with open(output_file, "w", encoding="utf-8") as f:
    f.write(data)

print(f"Файл перекодирован и сохранён как {output_file}")
