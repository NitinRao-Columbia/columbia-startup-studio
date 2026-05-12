**MVP\_doc**

**Core flow (user → action → value)**

* User creates a trip → invites friends → everyone marks availability and votes on destinations/activities → the app highlights the best dates and organizes selected activities into a realistic itinerary → the group ends up with a clear trip plan that everyone helped create.

**Tech stack**

* **Frontend:** React \+ react-dom  
* **Dev tooling:** Vite  
* **Styling:** Tailwind  
* **Backend / DB:** Supabase  
* **Maps / External APIs:** Google Maps  
* **Hosting / Deploy:** Vercel

**Team roles (who's building what, who's on demand gen)**

* Rebecca \- frontend web development  
* Thai \- frontend/backend integration  
* Elizabeth \- Demand generation, Landing Page, frontend  
* Luke \- database (supabase) \+ deployment

**What's faked (WoZ/concierge strategies)**

* **Fake auth:** test user and roles  
* **DB:** manually added data for recommendations  
* **Itinerary:** list of all locations split across time of trave for nowl, will adjust to find most optimal path for user to travel (based on distance)  
* **Calendar/availability:** Seed calendar availability with deterministic test data and provide UI controls to simulate conflicts

**Current demand gen status (what's running, what are the numbers)**

* Flyers and social media posts are made  
* Flyers will be posted around campus  
* Landing page up and running  
* Possibly try Reddit posts