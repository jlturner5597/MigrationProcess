<style>
body {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
}
h1, h2, h3, h4, h5, h6 {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #0078D7;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
}
h1 {
    font-size: 2.2em;
    text-align: center;
    border-bottom: 2px solid #0078D7;
    padding-bottom: 10px;
    margin-bottom: 30px;
}
h2 {
    font-size: 1.8em;
    border-bottom: 1px solid #eaecef;
    padding-bottom: 5px;
}
h3 {
    font-size: 1.5em;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    border-radius: 5px;
    overflow: hidden;
}
thead {
    background-color: #0078D7;
    color: white;
}
th, td {
    padding: 12px;
    text-align: left;
    border: 1px solid #ddd;
}
tr:nth-child(even) {
    background-color: #f8f9fa;
}
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 20px auto;
}
.note-box {
    background-color: #e1f5fe;
    border-left: 5px solid #0078D7;
    padding: 15px;
    margin: 20px 0;
}
.callout-box {
    background-color: #f8f9fa;
    border-left: 5px solid #0078D7;
    padding: 15px;
    margin: 20px 0;
}
.footer {
    background-color: #0078D7;
    color: white;
    padding: 20px;
    border-radius: 5px;
    margin-top: 30px;
    text-align: center;
}
.footer a {
    color: white;
    text-decoration: underline;
}
.toc {
    background-color: #f8f9fa;
    border: 1px solid #e9ecef;
    padding: 20px;
    border-radius: 5px;
    margin: 20px 0;
}
.toc h2 {
    text-align: center;
    border-bottom: none;
    margin-top: 0;
}
.toc a {
    color: #0078D7;
    text-decoration: none;
}
.toc a:hover {
    text-decoration: underline;
}
.header-logo {
    text-align: center;
    margin-bottom: 30px;
}
</style>

<div class="header-logo">
<img src="assets/SurpassPA_logo.png" alt="Surpass Logo" style="max-width: 350px;">
</div>

# Surpass Migration Framework: The Simple Guide

*A straightforward guide to moving your assessment system to Surpass*

<div class="toc">
<h2>Contents</h2>

<ol style="list-style-type: decimal; padding-left: 20px;">
  <li><a href="#quick-overview">Quick Overview</a></li>
  <li><a href="#the-big-picture">The Big Picture</a></li>
  <li><a href="#step-1-discovery--planning">Step 1: Discovery & Planning</a></li>
  <li><a href="#step-2-detailed-design">Step 2: Detailed Design</a></li>
  <li><a href="#step-3-building-it">Step 3: Building It</a></li>
  <li><a href="#step-4-testing-everything">Step 4: Testing Everything</a></li>
  <li><a href="#step-5-going-live">Step 5: Going Live</a></li>
  <li><a href="#timeline">Timeline</a></li>
  <li><a href="#wrapping-up">Wrapping Up</a></li>
</ol>
</div>

## Quick Overview

This guide explains how we move your assessment system to Surpass in a way that's organized but flexible. Think of it like moving to a new house - we need a plan, but we also need to adapt to your specific needs.

### What Makes Our Approach Great

<div class="callout-box">

- **Structured Process**: We break down the process into five manageable steps
- **Regular Check-ins**: We ensure alignment across all system components
- **Detailed Planning**: We map out exactly how everything should work
- **Efficient Tools**: We use specialized tools that streamline implementation
- **Comprehensive Testing**: We validate all aspects before going live

</div>

We give you a clear roadmap but can adjust to your unique situation. Each step builds on the previous one so nothing gets missed.

## The Big Picture

Our migration process follows five main steps with check-ins to make sure everything stays on track:

1. **Discovery & Planning**: Figure out what you need
2. **Detailed Design**: Create a detailed blueprint
3. **Building It**: Put everything together
4. **Testing Everything**: Make sure it all works
5. **Going Live**: Switch over to the new system

We'll check in regularly to make sure all parts of the system work well together.

```mermaid
flowchart TB
    A[Discovery & Planning] --> B[Detailed Design]
    B --> C[Building It]
    C --> D[Testing Everything]
    D --> E[Going Live]
    
    A -- "Check-in" --> F((Quality Control))
    B -- "Check-in" --> F
    C -- "Check-in" --> F
    D -- "Check-in" --> F
    
    style A fill:#0078D7,color:#fff
    style B fill:#0078D7,color:#fff
    style C fill:#0078D7,color:#fff
    style D fill:#0078D7,color:#fff
    style E fill:#0078D7,color:#fff
    style F fill:#f8f9fa,stroke:#0078D7,stroke-width:2px
```

<div style="text-align: center; font-style: italic; margin-bottom: 20px;">Figure 1: The Surpass Migration Journey - A structured approach with regular check-ins</div>

## Step 1: Discovery & Planning

<div class="note-box">
This happens before you sign a contract, so we understand what you need.
</div>

During this first step, we learn about your organization and what you need from your assessment system:

### Business Basics

<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; margin: 20px 0; border-radius: 5px; overflow: hidden;">
  <thead style="background-color: #0078D7; color: white;">
    <tr>
      <th style="padding: 12px; text-align: left; border: 1px solid #ddd;">What We Look At</th>
      <th style="padding: 12px; text-align: left; border: 1px solid #ddd;">What We Want to Know</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f8f9fa;">
      <td style="padding: 12px; border: 1px solid #ddd;"><strong>Your Organization</strong></td>
      <td style="padding: 12px; border: 1px solid #ddd;">Type of organization, industry, size, where you operate</td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid #ddd;"><strong>How You Work</strong></td>
      <td style="padding: 12px; border: 1px solid #ddd;">Current assessment processes, pain points, goals</td>
    </tr>
    <tr style="background-color: #f8f9fa;">
      <td style="padding: 12px; border: 1px solid #ddd;"><strong>Size of Program</strong></td>
      <td style="padding: 12px; border: 1px solid #ddd;">How many questions, test-takers, exams, and testing centers</td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid #ddd;"><strong>Your Team</strong></td>
      <td style="padding: 12px; border: 1px solid #ddd;">What technical resources and skills you have available</td>
    </tr>
  </tbody>
</table>
</div>

### Assessment Needs

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>What We Look At</th>
      <th>What We Want to Know</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Question Types</strong></td>
      <td>Multiple choice, essay, performance-based, multimedia</td>
    </tr>
    <tr>
      <td><strong>Media Needs</strong></td>
      <td>Images, audio, video, interactive elements</td>
    </tr>
    <tr>
      <td><strong>Exam Types</strong></td>
      <td>High/low stakes, clinical exams, digital/paper delivery</td>
    </tr>
    <tr>
      <td><strong>Test Structure</strong></td>
      <td>Fixed questions, dynamic questions, adaptive testing</td>
    </tr>
  </tbody>
</table>
</div>

### Technical Review

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>What We Look At</th>
      <th>What We Want to Know</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Delivery Method</strong></td>
      <td>Using Surpass directly or connecting to another system</td>
    </tr>
    <tr>
      <td><strong>Testing Technology</strong></td>
      <td>Web delivery, secure testing apps, browser requirements</td>
    </tr>
    <tr>
      <td><strong>Proctoring</strong></td>
      <td>Live monitoring, recording for review, or no proctoring</td>
    </tr>
    <tr>
      <td><strong>Testing Locations</strong></td>
      <td>Your own facilities or external testing centers</td>
    </tr>
    <tr>
      <td><strong>Connections</strong></td>
      <td>Systems that need to connect and share data</td>
    </tr>
    <tr>
      <td><strong>Hosting</strong></td>
      <td>Shared or dedicated system requirements</td>
    </tr>
    <tr>
      <td><strong>Custom Needs</strong></td>
      <td>Any gaps that need custom development</td>
    </tr>
  </tbody>
</table>
</div>

### What You Get

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What's Included</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Migration Plan</strong></td>
      <td>High-level approach to migration, potential phases</td>
    </tr>
    <tr>
      <td><strong>Timeline</strong></td>
      <td>Preliminary schedule with major milestones</td>
    </tr>
    <tr>
      <td><strong>Resources</strong></td>
      <td>Initial list of what resources you'll need</td>
    </tr>
    <tr>
      <td><strong>Risk Assessment</strong></td>
      <td>Identification of potential risks and how to handle them</td>
    </tr>
  </tbody>
</table>
</div>

## Step 2: Detailed Design

<div class="note-box">
After signing the contract, we create a detailed plan for implementation.
</div>

Now we dig deeper into exactly how everything should work:

### Requirements Gathering

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Area</th>
      <th>What We Create</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Business Requirements</strong></td>
      <td>Complete documentation of all your needs</td>
    </tr>
    <tr>
      <td><strong>Data Inventory</strong></td>
      <td>List of all data that needs to be moved</td>
    </tr>
    <tr>
      <td><strong>Current System</strong></td>
      <td>Map of your current processes and data</td>
    </tr>
    <tr>
      <td><strong>Future System</strong></td>
      <td>Map of how processes and data will work in Surpass</td>
    </tr>
  </tbody>
</table>
</div>

### Structure Planning

We plan the structure of your Surpass system with check-ins after each major component:

```mermaid
flowchart TD
    A[Organization Structure] --> B{Check}
    B -->|Pass| C[Question Bank Structure]
    C --> D{Check}
    D -->|Pass| E[Test Creation Structure]
    E --> F{Check}
    F -->|Pass| G[Test Administration]
    G --> H{Check}
    H -->|Pass| I[Reporting Structure]
    
    B -->|Revise| A
    D -->|Revise| C
    F -->|Revise| E
    H -->|Revise| G
    
    style A fill:#0078D7,color:#fff
    style C fill:#0078D7,color:#fff
    style E fill:#0078D7,color:#fff
    style G fill:#0078D7,color:#fff
    style I fill:#0078D7,color:#fff
    style B fill:#f8f9fa,stroke:#0078D7,stroke-width:2px
    style D fill:#f8f9fa,stroke:#0078D7,stroke-width:2px
    style F fill:#f8f9fa,stroke:#0078D7,stroke-width:2px
    style H fill:#f8f9fa,stroke:#0078D7,stroke-width:2px
```

<div style="text-align: center; font-style: italic; margin-bottom: 20px;">Figure 2: The Structure Planning Process - Ensuring quality at each stage</div>

#### Organization Structure Design

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What We Plan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Organization Setup</strong></td>
      <td>How to map your organization to Surpass</td>
    </tr>
    <tr>
      <td><strong>Sites/Centers/Subjects</strong></td>
      <td>How these elements relate to each other</td>
    </tr>
    <tr>
      <td><strong>Access Boundaries</strong></td>
      <td>Who can access what in the system</td>
    </tr>
  </tbody>
</table>
</div>

#### Question Bank Structure

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What We Plan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Bank Organization</strong></td>
      <td>How to organize your question banks</td>
    </tr>
    <tr>
      <td><strong>Question Metadata</strong></td>
      <td>How to tag and categorize questions</td>
    </tr>
    <tr>
      <td><strong>Workflow Setup</strong></td>
      <td>How questions move through creation and review</td>
    </tr>
    <tr>
      <td><strong>Media Handling</strong></td>
      <td>How to handle images, audio, and video</td>
    </tr>
  </tbody>
</table>
</div>

#### Test Creation Structure

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What We Plan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Test Settings</strong></td>
      <td>How tests will be configured</td>
    </tr>
    <tr>
      <td><strong>Development Process</strong></td>
      <td>How tests will be created and approved</td>
    </tr>
    <tr>
      <td><strong>Blueprint Mapping</strong></td>
      <td>How test blueprints connect to question selection</td>
    </tr>
  </tbody>
</table>
</div>

#### Test Administration

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What We Plan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Scheduling</strong></td>
      <td>How scheduling will work</td>
    </tr>
    <tr>
      <td><strong>Delivery Settings</strong></td>
      <td>How tests will be delivered securely</td>
    </tr>
    <tr>
      <td><strong>Security Requirements</strong></td>
      <td>What security measures will be in place</td>
    </tr>
  </tbody>
</table>
</div>

#### Reporting Structure

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What We Plan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Results Processing</strong></td>
      <td>How results will be calculated and processed</td>
    </tr>
    <tr>
      <td><strong>Analytics</strong></td>
      <td>What analytics and reporting you'll need</td>
    </tr>
    <tr>
      <td><strong>Data Export</strong></td>
      <td>How data will be exported and when</td>
    </tr>
  </tbody>
</table>
</div>

### Check-ins

Throughout this phase, we'll have check-ins to make sure everything works together:

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Review Area</th>
      <th>What We Check</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Data Compatibility</strong></td>
      <td>Is data structured correctly for all parts of the system?</td>
    </tr>
    <tr>
      <td><strong>Process Alignment</strong></td>
      <td>Do the workflows support your business needs?</td>
    </tr>
    <tr>
      <td><strong>Integration Viability</strong></td>
      <td>Are all connections between systems properly defined?</td>
    </tr>
    <tr>
      <td><strong>Performance</strong></td>
      <td>Will the design handle your expected volume?</td>
    </tr>
  </tbody>
</table>
</div>

### Migration Path

We'll determine the best way to move your data:

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Approach</th>
      <th>What We Consider</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>API Usage</strong></td>
      <td>Can we use automated connections?</td>
    </tr>
    <tr>
      <td><strong>Import Features</strong></td>
      <td>Can we use built-in import tools?</td>
    </tr>
    <tr>
      <td><strong>Manual Input</strong></td>
      <td>Do we need to enter some data manually?</td>
    </tr>
    <tr>
      <td><strong>Data Transformation</strong></td>
      <td>How complex is the data conversion?</td>
    </tr>
  </tbody>
</table>
</div>

### What You Get

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What's Included</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Migration Instructions</strong></td>
      <td>Step-by-step procedures for migration</td>
    </tr>
    <tr>
      <td><strong>Configuration Details</strong></td>
      <td>Complete specifications for system setup</td>
    </tr>
    <tr>
      <td><strong>Data Mapping</strong></td>
      <td>Documentation of how data will be transformed</td>
    </tr>
    <tr>
      <td><strong>Success Criteria</strong></td>
      <td>Clear definition of what success looks like</td>
    </tr>
  </tbody>
</table>
</div>

## Step 3: Building It

<div class="note-box">
This is when we actually start putting everything together.
</div>

Now we start building the system according to the plan:

### System Setup

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What We Do</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>System Configuration</strong></td>
      <td>Set up your Surpass instance</td>
    </tr>
    <tr>
      <td><strong>User Setup</strong></td>
      <td>Create administrative and test users</td>
    </tr>
    <tr>
      <td><strong>Connections</strong></td>
      <td>Set up connections to other systems</td>
    </tr>
  </tbody>
</table>
</div>

### Migration Tool Development

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What We Do</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Data Extraction</strong></td>
      <td>Create tools to get data from your current system</td>
    </tr>
    <tr>
      <td><strong>Transformation</strong></td>
      <td>Create tools to convert data to Surpass format</td>
    </tr>
    <tr>
      <td><strong>Loading</strong></td>
      <td>Create tools to load data into Surpass</td>
    </tr>
  </tbody>
</table>
</div>

```mermaid
flowchart LR
    A[Current System] --> B[Extract]
    B --> C[Transform]
    C --> D[Load]
    D --> E[Surpass]
    
    subgraph Migration Process
    B
    C
    D
    end
    
    style A fill:#f8f9fa,stroke:#333,stroke-width:1px
    style B fill:#0078D7,color:#fff
    style C fill:#0078D7,color:#fff
    style D fill:#0078D7,color:#fff
    style E fill:#f8f9fa,stroke:#333,stroke-width:1px
```

<div style="text-align: center; font-style: italic; margin-bottom: 20px;">Figure 3: The Data Migration Flow - Secure transformation of assessment data</div>

### Sample Content Creation

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What We Do</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Sample Content</strong></td>
      <td>Move a representative sample of content</td>
    </tr>
    <tr>
      <td><strong>Question Behavior</strong></td>
      <td>Test how questions behave</td>
    </tr>
    <tr>
      <td><strong>Media Handling</strong></td>
      <td>Verify that images, audio, and video work correctly</td>
    </tr>
  </tbody>
</table>
</div>

### What You Get

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What's Included</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Configured System</strong></td>
      <td>Fully configured Surpass instance</td>
    </tr>
    <tr>
      <td><strong>Tested Tools</strong></td>
      <td>Migration tools that have been tested</td>
    </tr>
    <tr>
      <td><strong>Test Data</strong></td>
      <td>Sample data that has been verified</td>
    </tr>
  </tbody>
</table>
</div>

## Step 4: Testing Everything

<div class="note-box">
We thoroughly test everything to make sure it works correctly.
</div>

We use different testing approaches to ensure everything works:

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Approach</th>
      <th>What We Test</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Manual Testing</strong></td>
      <td>User acceptance, process validation, configuration verification</td>
    </tr>
    <tr>
      <td><strong>Automated Testing</strong></td>
      <td>Data integrity, performance, integration</td>
    </tr>
    <tr>
      <td><strong>Cross-checking</strong></td>
      <td>Making sure all parts of the system work together</td>
    </tr>
  </tbody>
</table>
</div>

### What You Get

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What's Included</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Test Results</strong></td>
      <td>Documentation of all test results</td>
    </tr>
    <tr>
      <td><strong>Issue Resolution</strong></td>
      <td>Tracking of issues and how they were fixed</td>
    </tr>
    <tr>
      <td><strong>Your Approval</strong></td>
      <td>Documentation of your sign-off</td>
    </tr>
  </tbody>
</table>
</div>

## Step 5: Going Live

<div class="note-box">
This is when we switch over to the new system.
</div>

The final phase includes:

### Production Migration

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What We Do</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Data Migration</strong></td>
      <td>Move all your data to the new system</td>
    </tr>
    <tr>
      <td><strong>Verification</strong></td>
      <td>Final check of migrated data</td>
    </tr>
    <tr>
      <td><strong>Performance</strong></td>
      <td>Monitor system performance</td>
    </tr>
  </tbody>
</table>
</div>

### Knowledge Transfer

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What We Do</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Documentation</strong></td>
      <td>Provide all system documentation</td>
    </tr>
    <tr>
      <td><strong>Training</strong></td>
      <td>Complete user and admin training</td>
    </tr>
    <tr>
      <td><strong>Support</strong></td>
      <td>Set up ongoing support channels</td>
    </tr>
  </tbody>
</table>
</div>

### Project Wrap-up

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What We Do</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Lessons Learned</strong></td>
      <td>Document what we learned</td>
    </tr>
    <tr>
      <td><strong>Success Metrics</strong></td>
      <td>Report on project success</td>
    </tr>
    <tr>
      <td><strong>Follow-up</strong></td>
      <td>Plan for any follow-up activities</td>
    </tr>
  </tbody>
</table>
</div>

### What You Get

<div style="overflow-x: auto;">
<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>What's Included</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Working System</strong></td>
      <td>Fully migrated Surpass implementation</td>
    </tr>
    <tr>
      <td><strong>Trained Team</strong></td>
      <td>Your team trained on system use</td>
    </tr>
    <tr>
      <td><strong>Support</strong></td>
      <td>Established support channels</td>
    </tr>
  </tbody>
</table>
</div>

## Timeline

A typical migration project follows this schedule:


<div style="background-color: #f8f9fa; border: 1px solid #e9ecef; padding: 20px; border-radius: 5px; margin: 20px 0;">
<div style="text-align: center; margin-bottom: 15px; font-weight: bold; font-size: 1.2em; color: #0078D7;">Migration Timeline</div>

<div style="display: flex; flex-direction: column; gap: 10px;">
  <div style="display: flex; align-items: center;">
    <div style="width: 200px; font-weight: bold;">Discovery & Planning</div>
    <div style="flex-grow: 1; background-color: #0078D7; color: white; padding: 10px; border-radius: 4px; text-align: center;">2-3 months</div>
  </div>
  
  <div style="display: flex; align-items: center;">
    <div style="width: 200px; font-weight: bold;">Detailed Design</div>
    <div style="flex-grow: 0.8; background-color: #1E88E5; color: white; padding: 10px; border-radius: 4px; text-align: center;">1.5-2 months</div>
  </div>
  
  <div style="display: flex; align-items: center;">
    <div style="width: 200px; font-weight: bold;">Building It</div>
    <div style="flex-grow: 0.4; background-color: #3949AB; color: white; padding: 10px; border-radius: 4px; text-align: center;">3-4 weeks</div>
  </div>
  
  <div style="display: flex; align-items: center;">
    <div style="width: 200px; font-weight: bold;">Testing</div>
    <div style="flex-grow: 0.25; background-color: #5E35B1; color: white; padding: 10px; border-radius: 4px; text-align: center;">2-3 weeks</div>
  </div>
  
  <div style="display: flex; align-items: center;">
    <div style="width: 200px; font-weight: bold;">Going Live</div>
    <div style="flex-grow: 0.15; background-color: #8E24AA; color: white; padding: 10px; border-radius: 4px; text-align: center;">1-2 weeks</div>
  </div>
</div>
</div>

<div style="text-align: center; font-style: italic; margin-bottom: 20px;">Figure 4: Typical Migration Timeline - Comprehensive project planning</div>

<div class="note-box">
<strong>Note:</strong> Actual timelines may vary significantly based on your organization's specific needs, complexity, and resource availability. Some migrations can be completed more quickly, while more complex projects may require additional time.
</div>

1. **Discovery & Planning**: 2-3 months
   - Learning about your needs
   - Creating initial plans
   - Most time-intensive phase to ensure proper foundation

2. **Detailed Design**: 1.5-2 months
   - Gathering detailed requirements
   - Planning system structure
   - Creating migration instructions

3. **Building It**: 3-4 weeks
   - Setting up the environment
   - Developing migration tools
   - Creating test content

4. **Testing**: 2-3 weeks
   - Manual and automated testing
   - Validating all connections
   - Creating test reports

5. **Going Live**: 1-2 weeks
   - Final migration
   - Knowledge transfer
   - Project wrap-up

## Wrapping Up

Our Surpass Migration Framework gives you a clear, organized approach to moving to the Surpass platform while still being flexible enough to meet your unique needs. By following this framework, we can:

- Make sure we cover all the important parts
- Keep everything working together smoothly
- Check our work at each step
- Deliver a successful migration with minimal disruption

We're always improving our approach based on what we learn from each migration, so you get the benefit of our experience.

---

<div class="footer">
<h3>Ready to Get Started?</h3>
<p>Contact your Surpass representative today to begin your migration journey.</p>
<p>Email: <a href="mailto:info@surpass.com">info@surpass.com</a> | Phone: +1-555-SURPASS</p>
<p><em>Surpass: Assessment Without Barriers</em></p>
</div>