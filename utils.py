from openpyxl import load_workbook

def write_to_xlsx(a, b, c, d, e, f, g, k):
        fn = 'res.xlsx'
        wb = load_workbook(fn)
        ws = wb['info']
        ws.append([a, b, c, d, e, str(f), g, k])
        wb.save(fn)
        wb.close()