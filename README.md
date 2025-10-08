# Apple Org Structure – Sumble Take-Home

This project visualizes Apple’s internal org structure as inferred from job postings. The raw data included unstructured group and team names extracted from thousands of listings. My goal was to present this messy data in a clean, usable way — especially for non-technical GTM (go-to-market) users who rely on organizational clarity to prioritize outreach and plan strategy.

## Overview

I built a React + Tailwind web app that lets users explore Apple’s org hierarchy interactively. The app supports search, team exploration, and high-level insights through visual charts. Rather than just rendering raw data, I focused on designing a UI that would feel approachable and familiar to a sales or strategy user — someone who may not be technical, but needs to quickly find and understand how Apple structures its teams.

## Key Features

- **Searchable org structure:** Users can search by team or group name. Search filters results in real time and highlights both direct and partial matches.
- **Expandable hierarchy:** Each org group can be expanded to reveal its internal teams. This makes exploration feel lightweight instead of overwhelming.
- **Data cleaning:** Team and group names were inconsistent in the raw JSON, so I normalized them for clarity and consistency.
- **Visual insights:** I added a bar chart and donut chart to help users quickly spot the most active groups and understand team distribution at a glance.
- **Dashboard-style layout:** The design borrows patterns from modern SaaS admin tools to make the app feel familiar to GTM audiences. Everything is responsive and optimized for readability.

## Tech Stack

- React (with functional components and hooks)
- Tailwind CSS for layout and styling
- Chart.js via react-chartjs-2 for data visualization
- Manual data preprocessing in JavaScript (mocked `mentionCount` for visual insights)

## Design Considerations

Throughout the build, I made decisions with the non-technical user in mind. GTM teams aren’t looking for raw JSON structures — they need signals, clarity, and visual hierarchy. That’s why I prioritized searchable content, group/team expansion, and dashboard-style summaries over dense data tables or nested schemas.

## If I Had More Time

- I’d connect real mention frequencies (based on job post co-occurrence) rather than mocking them
- I’d add filters by role types, recency of postings, or location
- I’d explore highlighting “newly emerging” teams or org shifts over time
- I’d clean up overlapping/duplicate team names using fuzzy clustering or NLP-based deduplication

## Running the App

1. Clone the repo
2. Run `npm install`
3. Start the server with `npm start`
4. Visit `localhost:3000`

## Submission Notes

This app is best viewed as a working prototype — a slice of how Sumble might help GTM teams extract clarity from messy public data. I wanted to balance technical execution with empathy for the end user.

Thanks for taking the time to review it.
