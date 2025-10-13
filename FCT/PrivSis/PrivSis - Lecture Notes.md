# Systems Privacy – Comprehensive Lecture Notes (Lessons 1–5)

## Lesson 1 – Defining Privacy

### 1. Introduction

Privacy is a **multidisciplinary concept** encompassing law, philosophy, and computer science. Understanding privacy requires examining not just the _definition_ of privacy, but also its _purpose_ — protecting autonomy, human dignity, and freedom from manipulation.

### 2. Why Privacy Matters

- **Human right:** Recognized globally (e.g., UN Declaration of Human Rights, Article 12).
    
- **Enabling right:** Privacy enables freedom of thought, association, and recovery from past mistakes.
    
- **Digital threat:** Online tracking and data monetization make privacy harder to achieve.
    

**Example Scenarios:**

- A person’s past mistakes resurfacing online.
    
- Religious or political beliefs disclosed without consent.
    
- Old opinions preserved permanently through social media archives.
    

### 3. Defining Privacy

#### a. Privacy as Secrecy

- **Definition:** Information is private if kept completely secret.
    
- **Pros:** Simple and intuitive.
    
- **Cons:** Unrealistic — privacy is often shared selectively.
    
- **Example:** The _Third-Party Doctrine_ in U.S. law (information shared with third parties is no longer private).
    

#### b. Privacy as Autonomy Over Data

- **Definition:** Information is private if the individual controls how it’s used.
    
- **Pros:** Strong protections for data subjects.
    
- **Cons:** Ignores cases where privacy harms arise even with consent.
    
- **Foundation:** Basis for modern data protection frameworks like GDPR.
    

#### c. Solove’s Taxonomy (2005)

- Focuses on **privacy harms** instead of strict definitions.
    
- Groups harms into four categories:
    
    1. **Information Collection:** Surveillance, interrogation.
        
    2. **Information Processing:** Aggregation, identification, insecurity, secondary use, exclusion.
        
    3. **Information Dissemination:** Breach of confidentiality, exposure, blackmail, distortion.
        
    4. **Invasion:** Intrusion, decisional interference.
        

**Pros:**

- Rich framework of concrete harms.
    
- Captures legal and social dimensions.
    

**Cons:**

- Doesn’t strictly define privacy.
    
- Some harms depend on outcomes (e.g., disclosure).
    

#### d. Privacy as Contextual Integrity (Nissenbaum)

- **Core idea:** Privacy depends on whether information flows align with _social norms_.
    
- **Key parameters:**
    
    - Data sender, subject, recipient.
        
    - Information type.
        
    - Transmission principle (rules of disclosure).
        

**Example:**

- Teacher emailing a student their grade privately (acceptable).
    
- Teacher posting the grade publicly (violates contextual integrity).
    

**Critiques:**

- Social norms are subjective and context-dependent.
    
- Enforcement requires metadata for every interaction.
    

---

## Lesson 2 – Legal Frameworks for Privacy

### 1. Privacy by Policy vs Privacy by Design

- **By Policy:** Relies on trust (e.g., VPN provider’s policies). Fragile—can change anytime.
    
- **By Design:** Built into the system architecture (e.g., Tor network). Cannot be revoked without code change.
    

### 2. Data Minimization

- **Client-side:** Prevent data collection.
    
- **Server-side:** Limit storage, discard unnecessary data.
    

### 3. General Data Protection Regulation (GDPR)

- Enacted: **2016 (EU)**; foundational modern data protection law.
    
- Applies to: Any entity handling EU citizens’ personal data.
    

#### a. Key Definitions

- **Personal Data:** Any data identifying a natural person directly or indirectly.
    
- **Data Controller:** Decides how and why personal data is processed.
    
- **Data Processor:** Processes data on behalf of a controller.
    
- **Consent:** Must be freely given, informed, specific, and easy to withdraw.
    

#### b. The Seven Principles

1. **Lawfulness, Fairness, Transparency**
    
2. **Purpose Limitation** – Data used only for stated purposes.
    
3. **Data Minimization** – Collect only what’s necessary.
    
4. **Accuracy** – Keep data up to date.
    
5. **Storage Limitation** – Don’t retain data longer than needed.
    
6. **Integrity & Confidentiality** – Protect data against unauthorized access.
    
7. **Accountability** – Be able to demonstrate compliance.
    

#### c. The Eight Rights

1. **Be Informed** – Clear information about processing.
    
2. **Access** – Request and obtain personal data.
    
3. **Rectification** – Correct inaccurate data.
    
4. **Erasure** (“Right to be Forgotten”).
    
5. **Restrict Processing** – Temporarily limit use.
    
6. **Data Portability** – Transfer data between services.
    
7. **Object** – Stop certain processing (e.g., marketing).
    
8. **Automated Decision-Making & Profiling** – Right to human review.
    

**Technical Implications:**

- Must track data lineage, backups, and access logs.
    
- Need metadata flags for consent and restriction.
    
- Secure transmission (TLS, encryption) is mandatory.
    

### 4. GDPR Challenges

- Weak enforcement across countries.
    
- Dark patterns manipulating consent.
    
- Cookie banners misused for deceptive design.
    

### 5. California Consumer Privacy Act (CCPA)

- U.S. equivalent (2018), applies to for-profit entities.
    
- Similar to GDPR but **opt-out** model instead of opt-in.
    
- **Key Rights:**
    
    - Right to Know, Delete, Correct, Limit, and Opt Out.
        
    - Non-discrimination for exercising privacy rights.
        
- **Difference:** Consent is less explicit; relies on user opt-out signals.
    

---

## Lesson 3 – Web Tracking and Privacy Violations

### 1. Overview

Web tracking collects behavioral data through browsers, apps, and devices. Understanding these mechanisms helps design privacy-preserving systems.

### 2. Common Tracking Methods

|Method|Description|Mitigation|
|---|---|---|
|**IP Tracking**|Tracks via IP address (unique but shared).|Use VPNs or rotating IPs.|
|**Authentication Tracking**|Logged-in sessions identify behavior.|Separate accounts, limit login persistence.|
|**URL Parameters**|Track via query strings.|Remove parameters, use extensions.|
|**Cookies**|Store session and tracking data.|Disable 3rd-party cookies, use privacy browsers.|
|**Web Beacons**|Invisible pixels detect opens/views.|Block images, use secure email clients.|
|**Etag Tracking**|Uses browser cache identifiers.|Clear cache, private browsing.|
|**Browser Fingerprinting**|Derives identity from system configuration.|Use Tor/Brave, disable JS.|
|**Favicon Fingerprinting**|Uses cached favicons for tracking.|Disable favicon caching.|
|**JavaScript Tracking**|Monitors interactions and keys.|Block trackers via extensions.|
|**Location Tracking**|GPS, WiFi, or cell tower triangulation.|Disable location access.|

### 3. Data Brokers

- Aggregate data from public and commercial sources.
    
- Sell to advertisers and third parties.
    
- **Mitigation:** Exercise GDPR/CCPA rights to access or delete data.
    

### 4. Summary

- **The web was not designed for privacy.**
    
- Defense requires layered technical, behavioral, and legal strategies.
    

---

## Lesson 4 – Data Anonymization and Re-identification

### 1. De-identification

- **Pseudonymization:** Replace identifiers with random labels.
    
- **Suppression:** Remove identifying fields entirely.
    
- **Problem:** Data can often be re-identified by linking with other public datasets (linkage attack).
    

### 2. K-Anonymity

- Ensures each record is indistinguishable from at least _k–1_ others based on quasi-identifiers.
    
- **Techniques:** Suppression, Generalization, Top/Bottom coding.
    
- **Algorithm Example:** _Mondrian algorithm_ recursively partitions data to meet k-anonymity.
    

**Limitations:**

- **NP-hard** to optimize.
    
- Vulnerable to **homogeneity** and **background knowledge** attacks.
    

### 3. L-Diversity

- Requires each group of quasi-identifiers to contain at least _l_ distinct sensitive values.
    
- Mitigates homogeneity and background knowledge problems.
    
- **Attacks:** Skewness and similarity attacks still possible.
    

### 4. T-Closeness

- Ensures the distribution of sensitive attributes in each equivalence class is close to the overall distribution.
    
- Measures “information gain” to prevent adversaries from inferring sensitive data.
    

### 5. Limitations of These Methods

- Utility decreases with stronger privacy.
    
- Re-identification risk remains for correlated data.
    

---

## Lesson 5 – Differential Privacy (DP)

### 1. Concept

- Formal mathematical definition of privacy for algorithms, not just datasets.
    
- **Goal:** Ensure that output distributions of a function are nearly identical whether any individual’s data is included or not.
    

### 2. Key Definitions

- **Neighboring Datasets:** Differ by one individual’s data.
    
- **Mechanism:** Algorithm satisfying ε-DP.
    
- **Privacy Budget (ε):** Determines trade-off between privacy and accuracy.
    

### 3. Mechanisms for Differential Privacy

#### a. Randomized Response

- Add noise during **data collection**.
    
- Example: Coin-flip method for yes/no questions.
    

#### b. Laplace Mechanism

- Add noise during **query output** based on **global sensitivity** (maximum change in output from one record difference).
    

### 4. Sensitivity

- **Global Sensitivity (S):** Max |f(x) − f(x’)| for all neighboring datasets.
    
- **Example:**
    
    - COUNT query → S = 1.
        
    - SUM query → depends on value bounds (requires _clipping_).
        

### 5. Composition

- Multiple queries consume the privacy budget additively.
    
- **Parallel Composition:** Queries on disjoint datasets preserve ε.
    

### 6. Limitations

- Doesn’t protect against data leaks if raw data is stored.
    
- Privacy budget exhaustion limits repeated querying.
    
- Strong adversary models may reduce utility.
    

### 7. Comparison with K-Anonymity

|Aspect|K-Anonymity|Differential Privacy|
|---|---|---|
|**Scope**|Data-level|Algorithm-level|
|**Utility**|Often low|Tunable (via ε)|
|**Guarantee**|Structural|Probabilistic|
|**Protection**|Re-identification|Statistical inference|

---

## Summary for Exam Preparation

- **Understand definitions:** Secrecy, Autonomy, Solove, Contextual Integrity.
    
- **Be ready to explain GDPR rights and their technical implications.**
    
- **Know tracking mechanisms and mitigations.**
    
- **Be able to define and differentiate:** K-Anonymity, L-Diversity, T-Closeness, Differential Privacy.
    
- **Understand trade-offs:** Privacy vs Utility.
    

**Recommended readings:**

- Solove, _A Taxonomy of Privacy_ (2005)
    
- Nissenbaum, _Privacy as Contextual Integrity_
    
- EU GDPR (2016)
    
- _Programming Differential Privacy_ (Ch. 5–7)