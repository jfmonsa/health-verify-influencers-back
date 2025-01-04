# 🏥 Verify Health Influencers Admin Panel

Welcome to the "Verify Influencers" Admin Panel project! This README will guide you through the solution to the challenge of verifying health claims made by popular influencers. Our goal is to bring clarity and credibility to online health information by leveraging AI and credible scientific research.

## 🚀 Project Overview

### Problem Statement

With the abundance of health advice from various "experts" online, it can be challenging to discern trustworthy information. Our platform aims to verify health claims from influencers using credible scientific research, making it easier for people to find honest, evidence-based guidance.

### Solution

The admin panel automatically:

1. **Discovers and Analyzes Content**: Pulls recent health-related tweets and podcast transcripts for a given influencer.
2. **Identifies Health Claims**: Extracts health claims from the content and categorizes them.
3. **Verifies Claims**: Cross-references claims against reliable journals and assigns a verification status and trust score.
4. **Displays Results**: Presents the results in a clean, user-friendly interface.

## 🛠️ Tech Stack

### Backend

- **Python**: The core programming language.
- **FastAPI**: For building the API endpoints.
- **SQLModel**: As the ORM for database interactions.
- **Perplexity API**: For content analysis and claim verification, cross-referencing claims with scientific journals.

### Frontend

- **Typescript**: Core Programming Language.
- **Next.js**: For server-side rendering and building the frontend.
- **TailwindCSS**: For styling the UI components.
- **Shadcn UI**: For pre-built UI components.
- **Zod**: For schema validation.
- **React Query**: For data fetching and state management.

## 📚 High-Level Requirements

### Influencer Discovery

- Pull recent health-related tweets and podcast transcripts.
- Build a workflow to convert influencer content into health claims.
- Use AI to remove duplicate claims.

### Claim Verification

- Spot and categorize health claims.
- Cross-reference claims against reliable journals.
- Assign verification status (Verified, Questionable, Debunked) and trust score.

### Dashboard Display

- Leaderboard showing influencers, trust scores, follower counts, and claim stats.
- Influencer detail page listing all claims, verification status, and confidence scores.
- Research configuration page for setting date ranges, number of claims, and journals to use.

## 🖥️ Functional Demo

The admin panel allows users to input an influencer's name, run the "research," and see the results. The UI is designed based on provided mockups to ensure a clean and user-friendly experience.

## 🎥 Loom Video

Please check out my Loom video where I discuss:

- My favorite product I've built.
- What excites me most about this opportunity.
- My favorite AI tools for development and how I use them.

Let's make online health content more trustworthy together! 🌟
