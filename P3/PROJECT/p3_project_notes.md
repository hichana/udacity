GOALS AND MILESTONES:
* Parse, audit(for validity, accuracy, completeness, consistency, uniformity) and clean OpenStreetMap data
	* √Identify, archive, document Data File
	* √Inspect and document general structure 
	* √Speculate on what to work with specifically
	* √Inspect/audit/plan out cleaning methodology
	* √Build basic parser/CSV compiler
	* √Confirm basic parser/CSV compiler working properly
	* √Write cleaning scripts - insert into data.py
	* √Update schema - implement schema validation
	* Execute cleaning 

* Perform statistical analysis using database queries
	* port CSV files into database
	* investigate any other questions I may have
		* size of file
		* number of unique users
		* number of nodes and ways
		* number of chosen types of nodes, like cafes, shops, etc.
		* ...

* Report on how the data could be improved
	* Conduct at least one investigation to back up my suggestion
	* Discuss benefits and anticipated problems implementing the improvement




NOTES:
* Format - GitHub repo contains:
	* README.md (lists all files/folder in repo)
	* jupyter notebook (report)
		* two main sections:
			* short with results and visuals
			* long with tutorial/full report
		* Project narrative
			* discovery 
			* investigation
			* challenges while wrangling
			* results
			* ...
	* .txt
		* link to map position wrangled in project
		* intro and short description of area and why I chose it
	* scripts
		* Comprise one per field audited and one that converts and cleans all the data
	* supporting files folder (includes sample OSM file)

* Introductory notes
	* this will be also an exercise into the power of VIM
		* include link to VIM adventures game

* Statistical database investigation
	* possibly quantify
		* natural loss
		* loss to human property
		* ...

* Suggestions for improving data set
	* add elevation? Maybe already exists?

* Perform comment refactoring
	* my project
	* lesson quizes

* Why the hell is Lloyd's pond there?

---------------------------------------------------
	OpenStreetMap sounds like an important project. Their wiki describes the project:

	"Welcome to OpenStreetMap, the project that creates and distributes free geographic data for the world. We started it because most maps you think of as free actually have legal or technical restrictions on their use, holding back people from using them in creative, productive, or unexpected ways."

	From the OpenStreetMap [Map Features](http://wiki.openstreetmap.org/wiki/Map_Features) documentation page:

	"OpenStreetMap represents physical features on the ground (e.g., roads or buildings) using tags attached to its basic data structures (its nodes, ways, and relations). Each tag describes a geographic attribute of the feature being shown by that specific node, way or relation."

	So I'll be cleaning a node, way and/or a relation element. What are they exactly?

	Node:
	* "A node is one of the core elements in the OpenStreetMap data model. It consists of a single point in space defined by its latitude, longitude and node id."
	* "Nodes can be used to define standalone point features, but are more often used to define the shape or "path" of a way."
	* "Nodes can be used on their own to define point features. When used in this way, a node will normally have at least one tag to define its purpose."

	Way:
	* "A way is an ordered list of nodes which normally also has at least one tag or is included within a Relation."
	* "An open way is way describing a linear feature which does not share a first and last node. Many roads, streams and railway lines are open ways."
	* "An area (also polygon) is an enclosed filled area of territory defined as a closed way."

	Relation:
	* "A relation ... consists of one or more tags and also an ordered list of one or more nodes, ways and/or relations as members which is used to define logical or geographic relationships between other elements. "
	* "A member of a relation can optionally have a role which describes the part that a particular feature plays within a relation."
	* Relations may represent things like a bus route, an administrative boundary for a city, restrictions along a route such as "no left turn" or "no U-turn", etc.





---------------------------------------------------

