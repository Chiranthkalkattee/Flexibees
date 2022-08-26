import csv
from django.core.management.base import BaseCommand
from parse.forms import New_Emp,Employee_details_forms

 
class Command(BaseCommand):
    help = ("import csv local file");

    def add_arguments(self, parser):
        parser.add_argument("file_path", nargs=1, type=str)
    

    def handle(self, *args, **options):
        self.file_path = options["file_path"][0]
        self.prepare()
        self.main()
        self.finalize()

    def prepare(self):
        self.imported_counter = 0
        self.skipped_counter = 0
    
    def main(self):  
        self.stdout.write("importing Email")
        self.stdout.write("=======================")
        Name = []
        phone = []
        emails = []
        designation = []
        Emp_code = []
        filename = "scripts/processed_documents/records.csv" #csv file where we write
        filename1 = "scripts/processed_employee_document/records1.csv" #csv file where we write
        with open(self.file_path) as f :
            reader =list(csv.DictReader(f))
            for index, row_dict in enumerate(reader):
               
                Employee_name = row_dict["Employee_name"]
                Phone = row_dict["Phone_number"]
            #     email = row_dict["Email"]
            #     designation =row_dict["Designation"]
            #     emp_phone= row_dict["Phone_number"]
            #     emp_name = row_dict["Employee_name"]
            #     res = emp_name+emp_phone
                # Name.append({"Employee_name":Employee_name})
                # phone.append({"Phone":Phone})
            #     Emp_code.append({"Employee_code":res})
            #     emails.append({"Email":email})  #Email:chiranth1@gamil.com
            # print(emails)
            # print(Emp_code)
                row_dict['Employee_code'] =  Employee_name + Phone 
                emails.append(row_dict)
                print(emails)
               

        # # with open(filename, 'w' , newline='') as csvfile: 
            header = emails[0].keys()
            print(header)
        #     csvwriter = csv.DictWriter(csvfile,fieldnames = header) 
        #     csvwriter.writeheader() 
        #     csvwriter.writerows(emails)

        writer = csv.DictWriter(
                open(filename1, 'w',newline=''), fieldnames=header)

            # writing headers (field names)
        writer.writeheader()

            # writing data rows
        writer.writerows(emails)


    def finalize(self):
        self.stdout.write("=======================")