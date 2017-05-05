PROJECT GOALS AND MILESTONES:
* Parse and clean OpenStreetMap data
	* √Identify, archive, document Data File
	* √Research and document basic structure and use-case for Data File
	* √Prepare working sample of Data File
		* √Investigate structure of working sample (visually)
			* √lost structure of original b/c grabbing kth elem
				* EXP: find way to build sample that is cleaner
					* iterparse iterates over every elem/child
					* need iterate only over direct children
					* does element object have children?
	* Audit data(script)
		* √Identify focus
			* √going with natural features
		* √Create appropriate dict for auditing one or more features
			* √What keys exist? And what types of values do they hold?
		* Determine what to clean
			* One way elem (321535489) has incorrect keys (ex. "k=FCODE")
				* ok? There's only one...
			* Multiple values in values that are supposed to be unique
				* 4344824
			

	* Validity, accuracy, completeness, consistency, uniformity
	* Identify focus/scope for cleaning
	* Clean data(data.py-inspired script, uses audit script)
* Convert into database
* Perform statistical analysis using database queries of the data, investigate any other questions I may have
	* Ex
		* size of file
		* number of unique users
		* number of nodes and ways
		* number of chosen types of nodes, like cafes, shops, etc.
		* etc.
* Report on how the data could be improved - conduct at least one investigation to back up my suggestion - discuss benefits and anticipated problems implementing the improvement


PROJECT FORMAT:
* Readme (github repo)
	* lists all files/folder in repo
		* notebook/report
		* Text file with link to map position wrangled in project/short description of area and why chose it
		* scripts
		* supporting files


PROJECT NOTES:
* can use elevation tag to note how much of the natural area is below sea level
* currently - then find out when make some kind of count-down for how long
* people have to view it
* Project lives in github repo with README.md, but project is structured by a Jupyter notebook
* Project narrative of discovery, investigation, challenges while wrangling, results, etc. documented in the notebook
* Scripts comprise one per field audited and one that converts and cleans all the data
* Perform comment refactoring
	* my project
	* lesson quizes
* Focusing on New Orleans, which is expected to disappear within a finite period of time due to climate change
	* do some populated areas as main focus for project, find connection (ex. of a street name) within the populated area and then investigate unpoulated natural areas that will also disappear. Possibly quantify the natural loss (ex. number of aligators lost, bugs, effect of not having wetlands/marshes there anymore, etc.). Maybe find a programmatic way to name each stream and such? Maybe naming them will bring it home (what we're losing).
* NHD data seems clean already and well-sctuctured. Check!
* Why the hell is Lloyd's pond there? Maybe I can clean some or all of New Orleans, then do my stuff about natural areas?
* Possible suggestion for improving - YAML or some other markup is better? Maybe I demonstrate a way to parse XML into YAML). Analyze the possible pros and cons with the suggested improvements. Maybe suggest adding a tag that uses altitude to denote suseptability to climate change, or even drought. Basically another dimension to the openstreetmap that can make more apparent the effects of climate change.
* Andy suggests putting results way at top along with some graphics
* For report:
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

