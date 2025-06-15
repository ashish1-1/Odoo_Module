from odoo import fields, models
import logging,tempfile,binascii,xlrd

class FileUpload(models.Model):
    _name = 'csv.instance'
    _description = 'CSV Connector'

    name = fields.Char('Name', required=True)

    image = fields.Image(max_width=256, max_height=256)

    file = fields.Binary('File')

    model_id = fields.Many2one(string='Model', comodel_name='ir.model')

    
    field_column_mapping_ids = fields.One2many(
        string='Fields Column Mapping',
        comodel_name='field.column.mapping',
        inverse_name='instance_id',
    )
    

    def import_columns(self):
        message = self.env['message.message']
        if not self.file:
            return message.error("Excel File Missing, Please upload your excel file to import columns")
        try:
            fp = tempfile.NamedTemporaryFile(suffix=".xlsx")
            fp.write(binascii.a2b_base64(self.file))
            fp.seek(0)
            workbook = xlrd.open_workbook(fp.name)
            sheet = workbook.sheet_by_index(0)

            first_row = sheet.row_values(0)
        except Exception as e:
            return message.error(f"Message: {e}")
        col_lst = []
        col_obj = self.env['column.column']
        for col in first_row:
            col_exist = col_obj.search([('name', '=', col), ('instance_id', '=', self.id)])
            if not col_exist:
                col_lst.append({'name':col, 'instance_id': self.id})
        created_ids = col_obj.create(col_lst)
        if created_ids:
            return message.success(f"Successfully columns Import with {created_ids} Ids")
        return message.warning(f"No more columns to import")

        
    def import_operation(self):
        message = self.env['message.message']
        try:
            fp = tempfile.NamedTemporaryFile(suffix=".xlsx")
            fp.write(binascii.a2b_base64(self.file))
            fp.seek(0)
            workbook = xlrd.open_workbook(fp.name)
            sheet = workbook.sheet_by_index(0)

            
        except Exception as e:
            return message.error(f"Message: {e}")
        column_values = sheet.row_values(0)
        column_mappings = {}
        print("----------------Rows Values---------",column_values, self.field_column_mapping_ids.field_id.name)
        for col in column_values:
            col_map = self.env['column.column'].search([('name', '=', col),('instance_id', '=', self.id)])
            self.field_column_mapping_ids.search([('')])
        # for row_no in range(1, sheet.nrows):

    #     

    #     for row_no in range(sheet.nrows):
    #         if row_no <= 0:
    #             fields = map(lambda row:row.value.encode('utf-8'), sheet.row(row_no))
    #         else:
    #             line = list(map(lambda row:isinstance(row.value, str) and row.value.encode('utf-8') or str(row.value), sheet.row(row_no)))        
    #             record_check = self.env['mapping.record'].search(['csv_id','=',line[1]])
    #             if record_check:
    #                 message = "All Record are already Created" 
    #             else:
    #                 record_data = {'name':line[2],
    #                                'phone':line[3],
    #                                'email':line[4]}
    #                 record_create = self.env[self.model_name].create(record_data)
    #                 success.append(record_create.id)

    #                 mapping_data = {'odoo_id':record_create.id,
    #                                 'csv_id':line[1]}
    #                 mapping_record = self.env['mapping.record'].create(mapping_data)

    #                 message = f"Record Successfully Created with Id "+', '.join(map(str, success))

    #     return self.env['ow.message.wizard'].wizard_message(message)
