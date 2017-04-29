REQUIREMENTS
* Parse and clean open street map data for a part of the world
* Programmatically ssess data for:
    * Validity
    * Accuracy
    * Completeness
    * Consistency
    * Uniformity
* Compile data into an SQL database
* Use database queries to conduct a statistical overview of the dataset and run any other questions/analysis
* Report on how the data could be improved - conduct at least one investigation to back up the suggestion (ex. if I think YAML or some other markup is better - maybe I demonstrate a way to parse XML into YAML). Analyze the possible pros and cons with the suggested improvements.



EXECUTION
*@ Find/document data file
*@ Create smaller subset of data to work with - then test on larger set.
* Parsing
	* Manually inspect data, understand it's structure and document what I'll need to extract from it for the assessment stage



NOTES
* New Orleans, which is expected to disappear in a set number of years due to climate change
* Borrow and modify code from the open street map case study from lessons
* Check data accuracy, validity, etc. programmatically whenever possible, and fix it programmatically 
* Structure
	* Notebook is main report - should boil down to running one file in terminal that executes all cleaning, etc.
		* Overviewing the data, documenting the challenges encountered and thought process while data wrangling. Include visual checks and programmatic ones.
	* Scripts (one per field audited and one that converts and cleans the data) are in subfolder and imported/used/referenced in Jupyter notebook
	* Readme lists all files in folder
	* text file with link to map position wrangled in project/short description of area and why chose it
	* OSM sample
	* text file with citations and attribution
* Project scope
	* focus only on non-populated areas that will disappear. The populated areas are easy, because they will all basically be gone with global warming. So residents can just look around and count on it all going away. But who is going to look around at the natural areas? Who will remember a small river? How many actual animals, bugs, etc. will be displaced (can use this in statistical summary)? Many of these are nameless. Maybe i am the one who names them? Name them before they go away! Maybe naming them will make us more sad about their inevitable loss.
* Ask question and answer them with data
* Natural areas? Problem is that all the data is from NHD dataset and is probably already totall clean (and it's more simple). So how else can I both clean natural-related data and achieve my statement? Even many of the wetlands and such may not have names. Could there be a data-driven way to name them myself? Like why the hell is Lloyd's pond there? Maybe I can clean some or all of New Orleans, then do my stuff about natural areas?
* Check again that all problem sets from section are complete (probably omit the xml one with New York Times?). Comment, refactor if needed
