# CS498 Narrative Visualization Project

Narrative Visualization Project for Graduation Course

## Instructions and FAQ

* Are frameworks allowed?

  * we'll allow libraries to be used for the narrative visualization project, so long as these libraries are not used for the construction of any charts. For example, we will allow bootstrap, react, angular. We still insist on d3 only (plus HTML, CSS and SVG of course) for the charts, so for example annotations should be made by hand and not using an extension like d3-annotation

  * Projects that use these forbidden libraries for charts will lose up to 5% off their project grade.

  * ALLOWED topojson/leaflet

  * NOT ALLOWED d3 scale chromatic, d3-annotation, d3-geo-projection

* Your project will be graded best if you clearly stick to one of the forms: martini glass, interactive slide show or drill down story, and your scenes are individual pages.
  * Sticking closely to the form will better communicate to the TA's that you understand and can implement the concepts of narrative visualization.

* However, you could lose a few points for hardcoding data in your source code (which seems like it might be one function of r2d3), and you could also lose points for creating visualizations using software or libraries other than plain d3.js (which seems like it might be another use case for r2d3).

* I am using HTML to link to the next slide/scene.  I am also using HTML to indicate the "slide number" ("Slide 1/3", for example). Is the link considered a trigger since it calls the html that sets the next scene?  Is the slide number indicator a parameter even if it is just HTML text?

  * Yes, the link triggers a change in the scene parameter which then triggers a change in the slide indicator text parameter. Any element that changes values in your visualization, particularly when triggered by a user interaction, counts as a parameter. Be sure to describe the actual changes or action that take place when you click the link, rather than just stating that the link is a trigger. Triggers are the connections between parameters so you want to describe what and how parameters are actually changing.

## Tasks

* What questions do you want to answer?
* What is the problem you are trying to solve?
* What decisions are you trying to make?
* What outcomes are you hoping for?
* What story do you want to tell?
* What tasks should the viewer be able to perform?

## Essay

### Messaging

What is the message you are trying to communicate with the narrative visualization?

### Narrative Structure

* Which structure was your narrative visualization designed to follow (martini glass, interactive slide show or drop-down story)?
* How does your narrative visualization follow that structure? (All of these structures can include the opportunity to "drill-down" and explore. The difference is where that opportunity happens in the structure.)

### Visual Structure

* What visual structure is used for each scene?
* How does it ensure the viewer can understand the data and navigate the scene?
* How does it highlight to urge the viewer to focus on the important parts of the data in each scene?
* How does it help the viewer transition to other scenes, to understand how the data connects to the data in other scenes?

### Scenes

* What are the scenes of your narrative visualization?
* How are the scenes ordered, and why?

### Annotations

* What template was followed for the annotations, and why that template?
* How are the annotations used to support the messaging?
* Do the annotations change within a single scene, and if so, how and why?

### Parameters

* What are the parameters of the narrative visualization?
* What are the states of the narrative visualization?
* How are the parameters used to define the state and each scene?

### Triggers

* What are the triggers that connect user actions to changes of state in the narrative visualization?
* What affordances are provided to the user to communicate to them what options are available to them in the narrative visualization?

## Resources

opendoors <https://opendoorsdata.org/data/international-students/>

All Places of Origin <https://opendoorsdata.org/data/international-students/all-places-of-origin/>

Enrollment Trends <https://opendoorsdata.org/data/international-students/enrollment-trends/>

Leading Institutions <https://opendoorsdata.org/data/international-students/leading-institutions/>

Fields of Study <https://opendoorsdata.org/data/international-students/fields-of-study/>

Academic Level <https://opendoorsdata.org/data/international-students/academic-level/>

New International Student Enrollment <https://opendoorsdata.org/data/international-students/new-international-students-enrollment/>

Leading Places of Origin <https://opendoorsdata.org/data/international-students/leading-places-of-origin/>

Enrollment by Institutional Type <https://opendoorsdata.org/data/international-students/enrollment-by-institutional-type/>

Academic Level and Places of Origin <https://opendoorsdata.org/data/international-students/academic-level-and-places-of-origin/>

Fields of Study by Place of Origin <https://opendoorsdata.org/data/international-students/fields-of-study-by-place-of-origin/>

Leading Institutions by Instituation Type <https://opendoorsdata.org/data/international-students/leading-institutions-by-institutional-type/>

Primary Source of Funding <https://opendoorsdata.org/data/international-students/international-students-primary-source-of-funding/>
