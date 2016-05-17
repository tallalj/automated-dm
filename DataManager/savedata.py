class savedata:
    def __init__(self):
        print("data class initialized");

    def write_csv_to_json(self,csvFilePath,jasonFilePath):
        import csv
        import json
        # Open the CSV
        f = open(self.input_file, 'rU')
        # Change each fieldname to the appropriate field name. I know, so difficult.
        reader = csv.DictReader(f, fieldnames=("fieldname0", "fieldname1", "fieldname2", "fieldname3"))
        # Parse the CSV into JSON
        out = json.dumps([row for row in reader])
        # Save the JSON
        f = open(self.output_file, 'w')
        f.write(out)
        return self.output_file