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
        
    3. **Information Dissemination:** Breach of confidentiality, disclosure, exposure, increased accessibility, blackmail, appropriation, distortion.
        
    4. **Invasion:** Intrusion, decisional interference.
        

**Pros:**

- Rich framework of concrete harms. More complex then previous but still somewhat simple to apply
    
- Captures legal and social dimensions.
    

**Cons:**

- Doesn’t strictly define privacy.
    
- Some harms depend on outcomes (e.g., disclosure).
- Some harms are overly restrictive in their definition (e.g., decisional interference)


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

- **Personal Data:** Any data identifying a natural person directly or indirectly. Directly or indirectly identifiable through an identifier or combination of data points held
    
- **Data Controller:** Decides how and why personal data is processed.
    
- **Data Processor:** Processes data on behalf of a controller.
	
- Third Party: Other person/entity that under direct authority of the controller or processor, are authorised to process personal data.
	
- **Consent:** Must be freely given, informed, specific, and easy to withdraw.
    

#### b. The Seven Principles

 1. Lawfulness, Fairness, and Transparency:
	1. Processing the data can only occur if:
		Data Subject fully understands and consents
		To fulfill a contract with the data subject
		To fulfill a legal obligation
		For safety reasons
		For a public task in the public interest
		When the data owner or processor has an interest that:
			Is legitimate, and
			Cannot be overriden by rights of the data subject, and
			Is not objected to by the data subject, or the objection can be argued against
	
2. Purpose Limitation:
	1. Data must be collected and processed only for the stated purposes.
	2. To process data for other reasons, authorization is needed.
	
3. Data Minimization:
	1. Only process the minimum data needed to meet the purposes
	
4. Accuracy:
	1. The quality and accuracy of the data that is processed must be guaranteed.
	2. If the data is not accurate, the data subject has the right to update the data.
	
5. Storage Limitations:
	1. Data cannot be held for longer than is required.
	2. Indefinite storage is allowed in the case of:
		Archiving for the public interest
		Scientific or historical research purposes
		Statistical purposes
	
6. Integrity and Confidentiality:
	1. The secure processing of data, i.e. protecting the data from data breaches or malicious edits
	
7. Accountability:
	1. Data Controllers and Data Processors must be able to demonstrate compliance
	2. If there is an unauthorized disclosure, it must be reported and there need to have been reasonable safeguards against it.
    

#### c. The Eight Rights

1. Be informed:
	– Clear, succinct, and easily understandable about how data is processed
	
	– Name and contact of organization, representative, data protection officer
	
	– Purposes of collection and processing
	
	– Legitimate interests for processing
	
	– Retention periods
    
2. Rectification
	– Correct incorrect data
	
	– Complete incomplete data
	
	– Can be done verbally or in writing
	
	– Requires a response in one month.
    
3. Access
	– Right to request access to their own data
	
	– Companies have one month to respond
	
	– No fee can be charged
	
	– Businesses must verify the identity of the requester
    
4. Erasure
	– Right to request data be erased
	
	– Companies have one month to respond
	
	– Not absolute – if a legal reason is requiring the data to be held, it cannot be deleted.
	
	– Marking for deletion is OK as long as it is deleted in a reasonable amount of time.
    
5. Restrict Processing of your data
	– Ask for the restriction or suppression of personal data.
	
	– Companies can store data, but cannot process it in any other way.
	
	– Not absolute.
	
	– Companies have one month to respond.
    
6. Data Portability
	– Copy, transfer or move personal data from one online environment to another, safely and securely
    
7. Object 
	– Right to object to their data being used for marketing reasons
	
	– Right to object to use of data for other purposes
		If the company has a compelling reason to continue, it may.
    
8. Automated Profiling and Decision Making
	– If the processor is:
		acting solely on automated decision-making, and
		This decision-making has a significant effect on the individual
	
	– If so, the processor must:
		Tell the subject about the processing
		Have and communicate easy ways to challenge automated decisions
		Ask for humans to verify the decision
		Check the system regularly and often
    

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

| Method                      | Description                                 | Mitigation                                       |
| --------------------------- | ------------------------------------------- | ------------------------------------------------ |
| **IP Tracking**             | Tracks via IP address (unique but shared).  | Use VPNs or rotating IPs.                        |
| **Authentication Tracking** | Logged-in sessions identify behavior.       | Separate accounts, limit login persistence.      |
| **URL Parameters**          | Track via query strings.                    | Remove parameters, use extensions.               |
| **Cookies**                 | Store session and tracking data.            | Disable 3rd-party cookies, use privacy browsers. |
| **Web Beacons**             | Invisible pixels detect opens/views.        | Block images, use secure email clients.          |
| **Etag Tracking**           | Uses browser cache identifiers.             | Clear cache, private browsing.                   |
| **Browser Fingerprinting**  | Derives identity from system configuration. | Use Tor/Brave, disable JS.                       |
| **Favicon Fingerprinting**  | Uses cached favicons for tracking.          | Disable favicon caching.                         |
| **JavaScript Tracking**     | Monitors interactions and keys.             | Block trackers via extensions.                   |
| **Location Tracking**       | GPS, WiFi, or cell tower triangulation.     | Disable location access.                         |

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
Removes identifiers
Ensure that no quasi-identifier appears less than k times

- Ensures each record is indistinguishable from at least _k–1_ others based on quasi-identifiers.
    
- **Techniques:** 
	- Suppression
		– Removing information or parts of information.

	 -  Generalization
		– Placing values into bins and only showing the bins

	- Top and Bottom Coding
		– Setting all extreme outliers to a maximum or minimum number
    
- **Algorithm Example:** _Mondrian algorithm_ recursively partitions data to meet k-anonymity:
	  We anonymize by using the suppression or generalization
		– Suppression is easy
		– Generalization for quantitative values are easy
			-Range
			-Mean
			-Median
		– Generalization for qualitative values is harder 
			- requires a programmer-defined generalization hierarchy.
    

**Limitations:**

- **NP-hard** to optimize.
    
- Vulnerable to **homogeneity** and **background knowledge** attacks.
    

### 3. L-Diversity
Attempts to avoid homogeneity and background knowledge attacks.
Is meant to be used with k-anonymity.

- Requires each group of quasi-identifiers to contain at least _l_ distinct sensitive values.
    
- Further loss of utility
	Privacy issues still exist
		– Attribute Disclosure: Knowing an identity, gain info about an attribute
		– Identity Disclosure: Link an individual to their row in the DB
- Skewness attack
		– Leads to attribute disclosure
		– Skews in the data itself can reveal information, even in l-diverse tables
- Similarity attack
		– Leads to attribute disclosure
		– Similar but distinct sensitive values can lead to privacy leakage, even with l-diversity.

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
    ![[Pasted image 20251017110053.png]]

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



# EXAMPLE TEST 1 :

1. (2.00 points) Describe Privacy as Autonomy over Data in your own words.

	1. The data is considered private if the data subject considers the data private. The data cannot be used if the subject does not allow.

2. (3.00 points) Name two principles of the GDPR and describe them in your own words.
	1. Lawfulness, Fairness, and Transparency:
		1. Processing the data can only occur if:
			Data Subject fully understands and consents
			To fulfill a contract with the data subject
			To fulfill a legal obligation
			For safety reasons
			For a public task in the public interest
			When the data owner or processor has an interest that:
				Is legitimate, and
				Cannot be overriden by rights of the data subject, and
				Is not objected to by the data subject, or the objection can be argued against
	2. Purpose Limitation:
		1. Data must be collected and processed only for the stated purposes.
		2. To process data for other reasons, authorization is needed.
	3. Data Minimization:
		1. Only process the minimum data needed to meet the purposes
	4. Accuracy:
		1. The quality and accuracy of the data that is processed must be guaranteed.
		2. If the data is not accurate, the data subject has the right to update the data.
	5. Storage Limitations:
		1. Data cannot be held for longer than is required.
		2. Indefinite storage is allowed in the case of:
			Archiving for the public interest
			Scientific or historical research purposes
			Statistical purposes
	6. Integrity and Confidentiality:
		1. The secure processing of data, i.e. protecting the data from data breaches or malicious edits
	7. Accountability:
		1. Data Controllers and Data Processors must be able to demonstrate compliance
		2. If there is an unauthorized disclosure, it must be reported and there need to have been reasonable safeguards against it.

3. In this class we learned about k-anonymity, a method to protect data from re-identification attacks. In your own words, please define the following terms related to k-anonymity:
	1. (0.50 points) Suppression:
		1. Removing identifying or quasi-identifying values from a dataset to prevent re-identification.
	2. (0.50 points) Add-remove adjacency
		1. Two datasets are **add-remove adjacent** (neighbors) they differ by **exactly one record** (one person’s data added or removed).
	3. (2.00 points) k-anonymity
		1. A dataset satisfies **k-anonymity** if **each unique combination of quasi-identifiers appears in at least _k_ records.**  This ensures that each individual is **indistinguishable among at least (k–1) others.**
			**Goal:** Prevent re-identification using linkage attacks.  
			**Limitations:** Vulnerable to _homogeneity_ and _background knowledge_ attacks.

4. (5.00 points) Consider the following data:

	ID Date Amount Currency Merchant Category Risk Level
	
	1 15/1/2020 9446,82 AZN Food - Frozen Foods 3
	
	2 11/3/2024 2672,26 PLN Home Improvement 1
	
	3 20/12/2020 2574,14 EUR Electronics 2
	
	4 17/9/2020 4065,55 THB Food - Canned Goods 4
	
	5 19/2/2019 1125,05 EUR Clothing - Tops 5
	
	6 19/3/2020 343,57 PLN Accessories 1
	
	7 5/4/2025 1534,57 EUR Food - Frozen Foods 5
	
	Consider the final attribute to be the sensitive value, the ID to be purely operational (and therefore does not need to be modified) and the rest to be the QID. 2-anonymize the data. Justify any categorical substitutions you may have made, and discuss the utility of the resulting data.

5. (3.00 points) Consider a dataset containing the following attributes collected from different regions of Portugal:

	Age, postal code, height (in cm), marital status, and education level. 
	
	Suppose that we wish to perform a query that calculates the average height a person may have, but we want it to be a 0.3-differentially private mechanism using the Laplace method. What is the noise that you need to inject into the query response? 
	
	I am expecting the answer as a formula, but with the parameters defined. Therefore, you must calculate the value of the sensitivity, which may or may not require clipping. If it does, you may be required to make a judgement call about a reasonable cut-off for a field’s bounds. Please justify any of these judgement calls.


	**5. Differential Privacy – Laplace Noise (3 pts)** \n\nWe want a **0.3-DP mechanism** for average height.\n\n#### **Step 1: Define query** \n\( f(x) = \text{AVG(Height)} \)\n\n#### **Step 2: Sensitivity (Δf)** \nFor averages: \n\( \Delta f = \frac{\text{max height} - \text{min height}}{n} \)\n\nAssume reasonable human height bounds:\n- min = 50 cm\n- max = 250 cm\n\n\( \Delta f = (250 - 50) / n = 200/n \)\n\n#### **Step 3: Laplace Mechanism**\nNoise added: \n\[\n\text{Noise} \sim Laplace(0, b) \quad \text{where} \quad b = \frac{\Delta f}{\epsilon}\n\]\n\nSo:\n\[\n\boxed{Noise \sim Laplace(0, 200 / (n \times 0.3))}\n\]\n\nIf dataset size n = 100 → \n\( b = 200 / 30 = 6.67 \)\n\n#### **Interpretation:** \nAdd Laplace noise with scale 6.67 cm to the query response.\n\n> Justification: Using clipping ensures sensitivity is bounded by plausible human limits.\n\n---\n\n###

6. (2.00 points) Describe how web beacon tracking works in your own words.
		Web beacons (a.k.a. pixel tags) are **tiny invisible images** (often 1×1 px) embedded in web pages or emails. When loaded, they **send a request to the server**, revealing:
		 IP address, Time of opening, Device and user agent
		Possibly referrer information used for **email open tracking** and **ad analytics**.
		**Mitigation:** Block images by default or use privacy extensions that block trackers.

7. (2.00 points) Can a dataset be differentially private? If so, how? If not, why not?
		A dataset can only be called “differentially private” if it was **produced by** a DP algorithm—meaning randomness was introduced during data collection or query output.
		**Summary:** DP protects _outputs_, not static datasets.