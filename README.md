Zac Capell<br>
4/29/2020<br>
Heavywater Front End Engineer Test notes<br>

Requirements met:<br>
    - Main page:<br>
        - Classification button leads to classifications page<br>
        - Extraction button leads to extractions page<br>
    - Classifications page:<br>
        - Clients and documents can be selected from drop down menus<br>
        - Can locate the document given for the client given, works with multiple document and client names<br>
        - Can update a value for any extant document type for any client<br>
        - Ability in code to export results as CSV document<br>
    - Extractions page:<br>
        - Drop down menu to select a single document type<br>
        - Extracts and sorts all fields into defined groups, in datapoint order given<br>
        - Ability exists to define new group number and datapoint order for a given field<br>
        - Ability exists to export all fields as CSV<br>
        - Ability exists to export fields for one document as TXT list<br>

Requirements not met:<br>
    - Most UIs are very bare<br>
    - Classifications page:<br>
        - Selecting multiple clients or documents does not work as expected and only process the lowest on the list
        - Updating values is done as a GET instead of a PUT or POST<br>
        - Data is displayed in raw JSON form<br>
            - This stops PDFs from being displayed<br>
        - Updates require their own separate page<br>
        - Currently no function to define new document types or clients in front end<br>
    - Extractions page:<br>
        - Fields are shown as raw JSON<br>
        - Rearranging is not possible through front end due to lack of UI<br>
        - All fields CSV prints in rows, not columns<br>
