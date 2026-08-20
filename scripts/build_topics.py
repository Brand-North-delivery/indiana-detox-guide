#!/usr/bin/env python3
"""Generate static, source-backed topic pages for the Indiana Detox Guide."""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://indianadetoxguide.com/"
REVIEWED = "August 19, 2026"

CLUSTER_IMAGES = {
    "Treatment guides": {
        "file": "treatment-consultation-room.png",
        "alt": "Two green chairs and a wood table in an empty consultation room with trees visible through a window.",
        "caption": "Guide-created editorial image of a consultation setting; it does not depict a specific Indiana facility.",
    },
    "Substance guides": {
        "file": "substance-treatment-paths.png",
        "alt": "An open blank notebook beside wooden markers arranged as branching paths on a green cloth.",
        "caption": "Guide-created editorial image illustrating treatment decision paths; it does not depict a clinical service or facility.",
    },
    "Planning guides": {
        "file": "rehab-admission-planning.png",
        "alt": "A canvas overnight bag, folded clothes, plain folder, blank identification card, and phone arranged on a bench.",
        "caption": "Guide-created editorial image illustrating admission preparation; facility packing rules vary.",
    },
    "Family and recovery": {
        "file": "family-recovery-conversation.png",
        "alt": "Two empty chairs and two mugs arranged for a conversation beside a window overlooking a garden.",
        "caption": "Guide-created editorial image illustrating a supportive conversation; it does not depict a specific person or facility.",
    },
}

SOURCES = {
    "samhsa-treatment": ("SAMHSA: Learn About Treatment", "https://www.samhsa.gov/find-support/learn-about-treatment"),
    "asam": ("ASAM Criteria Fourth Edition", "https://www.asam.org/asam-criteria/asam-criteria-4th-edition"),
    "niaaa": ("NIAAA: Types of Alcohol Treatment", "https://alcoholtreatment.niaaa.nih.gov/what-to-know/types-of-alcohol-treatment"),
    "niaaa-quality": ("NIAAA: Finding Quality Alcohol Treatment", "https://alcoholtreatment.niaaa.nih.gov/how-to-find-alcohol-treatment"),
    "samhsa-family": ("SAMHSA: Helping Families Cope", "https://www.samhsa.gov/mental-health/children-and-families/coping-resources"),
    "samhsa-recovery": ("SAMHSA: Recovery and Support", "https://www.samhsa.gov/substance-use/recovery"),
    "asam-benzo": ("ASAM: Benzodiazepine Tapering", "https://www.asam.org/quality-care/clinical-guidelines/benzodiazepine-tapering"),
    "samhsa-moud": ("SAMHSA: Medications for Substance Use Disorders", "https://www.samhsa.gov/substance-use/treatment/options"),
    "medicare": ("Medicare: Mental Health and Substance Use Coverage", "https://www.medicare.gov/coverage/mental-health-substance-use-disorder"),
    "indiana": ("Indiana DMHA Provider Information", "https://secure.in.gov/fssa/dmha/quality-assurance-quality-improvement/mental-health-and-addiction-providers/"),
}

TOPICS = [
    {
        "slug": "alcohol-rehab", "cluster": "Treatment guides", "title": "Alcohol Rehab in Indiana", "description": "Learn how alcohol rehab works, compare levels of care, and prepare questions for Indiana treatment providers.",
        "answer": "Alcohol rehab is organized treatment for alcohol use disorder and alcohol-related problems. Care may combine assessment, behavioral treatment, medications, withdrawal management, and continuing support at an outpatient, residential, or inpatient level selected for the person's needs.",
        "facts": [("Assessment comes first", "Alcohol use, withdrawal history, medical and mental health conditions, other substances, home support, and prior treatment can change the appropriate plan."), ("Detox and rehab are different", "Withdrawal stabilization may be necessary, but ongoing treatment addresses the patterns, health needs, and recovery supports connected to alcohol use."), ("Evidence-based care has options", "Professionally led alcohol treatment can include behavioral therapies, prescribed medications, or both."), ("Intensity should match need", "Outpatient, intensive outpatient, residential, and medically directed inpatient care serve different clinical situations.")],
        "questions": ["Who completes the assessment and how is withdrawal risk evaluated?", "Which medications and behavioral therapies are available?", "How does care continue after the initial program?"],
        "faqs": [("Does everyone need inpatient alcohol rehab?", "No. A qualified assessment should guide intensity. Some people can receive outpatient care, while others need residential or medically directed services."), ("Is alcohol detox enough by itself?", "Usually not as a complete recovery plan. Detox addresses withdrawal and stabilization; rehabilitation and continuing care address longer-term needs."), ("Can medications be part of alcohol treatment?", "Yes. Qualified prescribers may use approved medications as one component of an individualized plan."), ("How do I compare Indiana alcohol programs?", "Verify credentials, assessment practices, evidence-based treatment, medical capability, customized planning, and continuing recovery support.")],
        "related": ["alcohol-detox", "medical-detox", "inpatient-rehab", "outpatient-rehab", "rehab-cost", "relapse-prevention"], "sources": ["niaaa", "niaaa-quality", "asam", "indiana"], "grove": ("Explore The Grove Estate's residential rehab program", "https://grovetreatment.com/programs/rehab/")
    },
    {
        "slug": "drug-rehab", "cluster": "Treatment guides", "title": "Drug Rehab in Indiana", "description": "Understand drug rehab, treatment settings, medications, therapies, and questions for Indiana providers.",
        "answer": "Drug rehab is an umbrella term for organized treatment and recovery services addressing problematic drug use. A plan may include medical assessment, withdrawal management, medications for certain disorders, counseling, residential or outpatient care, and continuing support.",
        "facts": [("The substance matters", "Opioids, stimulants, benzodiazepines, cannabis, alcohol, and polysubstance use can create different treatment and safety needs."), ("Placement is individualized", "ASAM uses multidimensional assessment to match clinical needs with an appropriate level of care."), ("Treatment is more than abstinence monitoring", "Good plans address physical health, mental health, recovery environment, medications, behavior, and practical barriers."), ("Continuity matters", "Transitions between detox, residential, outpatient, medications, peer support, and recovery housing should be planned rather than improvised.")],
        "questions": ["Which substances and co-occurring conditions can this location treat?", "Which services are delivered on site versus by referral?", "What is the written transition and continuing-care plan?"],
        "faqs": [("Is drug rehab always residential?", "No. Treatment can be outpatient, intensive outpatient, residential, or inpatient depending on assessment and available services."), ("Does drug rehab include detox?", "Some programs provide withdrawal management, while others require stabilization elsewhere. Confirm the exact location and level."), ("Can medication be part of drug rehab?", "Yes for certain substance use disorders and clinical needs. Ask who prescribes and how medication continues after discharge."), ("What should I verify in Indiana?", "Check state credentials, accreditation claims, clinical staffing, location-specific services, emergency transfer plans, and payment terms.")],
        "related": ["medical-detox", "inpatient-rehab", "outpatient-rehab", "dual-diagnosis-treatment", "opioid-rehab", "rehab-admissions-process"], "sources": ["samhsa-treatment", "asam", "indiana"], "grove": ("Explore The Grove Estate's residential rehab program", "https://grovetreatment.com/programs/rehab/")
    },
    {
        "slug": "medical-detox", "cluster": "Treatment guides", "title": "Medical Detox in Indiana", "description": "Learn what medical detox does, who may need monitoring, and how to verify Indiana detox capabilities.",
        "answer": "Medical detox is clinical evaluation, monitoring, and treatment for intoxication or withdrawal risk. It can include symptom scoring, medications, nursing observation, medical management, and transfer planning, but the exact capability varies by facility and level of care.",
        "facts": [("Withdrawal risk is substance-specific", "Alcohol and benzodiazepine withdrawal can become medically dangerous; opioids and other substances create different symptom and medication needs."), ("A label is not proof", "A website saying detox does not establish staffing, overnight coverage, medication protocols, or emergency capability."), ("Assessment determines placement", "Current use, prior complications, health conditions, pregnancy, medications, mental health, and home environment all matter."), ("Stabilization needs a next step", "A discharge or transfer plan should connect detox to ongoing treatment and recovery support.")],
        "questions": ["Who is physically present overnight and who can prescribe?", "Which withdrawal syndromes can be managed at this address?", "Where and how does an emergency transfer occur?"],
        "faqs": [("Is medical detox the same as rehab?", "No. Detox focuses on intoxication and withdrawal stabilization. Rehab is a broader treatment process."), ("Can detox happen outpatient?", "Some lower-risk situations may be managed in outpatient medical settings, while others require residential or inpatient monitoring."), ("How long does detox take?", "There is no universal duration. Substance, use pattern, health, symptoms, medications, and response to treatment affect timing."), ("What should I bring to detox?", "Follow the facility's current list. Bring identification, insurance information, approved medications in original packaging, and essential contacts unless told otherwise.")],
        "related": ["alcohol-detox", "benzo-rehab", "opioid-rehab", "inpatient-rehab", "rehab-admissions-process", "what-to-pack-for-rehab"], "sources": ["asam", "samhsa-treatment", "indiana"], "grove": ("View The Grove Estate's medical detox program", "https://grovetreatment.com/programs/detox/")
    },
    {
        "slug": "alcohol-detox", "cluster": "Substance guides", "title": "Alcohol Detox in Indiana", "description": "Understand alcohol withdrawal risk, medical detox questions, and next-step planning in Indiana.",
        "answer": "Alcohol detox is the process of stopping alcohol use while evaluating and treating withdrawal. Because alcohol withdrawal can become severe or life-threatening, a qualified clinician should assess risk rather than relying on a website checklist or attempting abrupt withdrawal without guidance.",
        "facts": [("History changes risk", "Prior seizures, delirium, repeated withdrawals, heavy use, medical illness, other sedatives, and pregnancy can affect placement."), ("Symptoms can change", "Withdrawal severity can evolve, so monitoring and a clear escalation plan matter."), ("Medication decisions are clinical", "Facilities differ in protocols, prescribing authority, and monitoring capability."), ("Detox is the opening phase", "Alcohol treatment may continue with behavioral therapies, medications, residential or outpatient services, and recovery support.")],
        "questions": ["How is alcohol withdrawal severity measured and reassessed?", "What medical and nursing coverage is available overnight?", "What treatment begins after stabilization?"],
        "faqs": [("Can alcohol withdrawal be dangerous?", "Yes. Severe withdrawal can be a medical emergency. Call 911 for seizures, severe confusion, breathing problems, collapse, or immediate danger."), ("Should alcohol be stopped suddenly at home?", "A clinician should assess the situation, especially with regular heavy use or previous withdrawal complications."), ("Does every rehab provide alcohol detox?", "No. Some provide it on site; others arrange hospital or separate detox before admission."), ("What follows alcohol detox?", "The next plan may include medication, counseling, residential or outpatient treatment, mutual support, and medical follow-up.")],
        "related": ["alcohol-rehab", "medical-detox", "inpatient-rehab", "dual-diagnosis-treatment", "rehab-admissions-process", "relapse-prevention"], "sources": ["niaaa", "asam", "indiana"], "grove": ("View The Grove Estate's medical detox program", "https://grovetreatment.com/programs/detox/")
    },
    {
        "slug": "inpatient-rehab", "cluster": "Treatment guides", "title": "Inpatient and Residential Rehab in Indiana", "description": "Compare inpatient and residential addiction treatment, clinical intensity, and Indiana provider questions.",
        "answer": "Inpatient and residential rehab both involve overnight care, but they are not interchangeable labels. Inpatient treatment is generally hospital-based or medically directed, while residential treatment provides a 24-hour living setting with clinical intensity and medical capability that vary by program.",
        "facts": [("Setting and capability differ", "Ask whether the program is hospital-based, medically managed residential, or clinically managed residential."), ("Twenty-four-hour residence is not twenty-four-hour medical care", "Verify who is present by shift and what medical services are actually delivered."), ("Structure can support stabilization", "A predictable environment may help when outpatient care or the home setting cannot safely meet current needs."), ("Length is not a quality score", "Duration should follow assessment, progress, coverage, and transition needs rather than a universal promise.")],
        "questions": ["What licensed level of care is delivered at this exact address?", "Which clinicians and nurses are present by shift?", "How is discharge coordinated with outpatient and medication care?"],
        "faqs": [("Is residential rehab a hospital?", "Usually not. Residential programs are non-hospital living settings, although some have substantial medical capability."), ("Does inpatient rehab include detox?", "It may, but not automatically. Confirm withdrawal-management services and staffing at the location."), ("Are private rooms guaranteed?", "No. Confirm room type, availability, cost, and what happens if placement changes."), ("How should families compare programs?", "Compare clinical fit, credentials, staffing, therapies, medical access, communication, environment, cost, and continuing care.")],
        "related": ["outpatient-rehab", "medical-detox", "how-long-is-rehab", "what-to-pack-for-rehab", "rehab-cost", "dual-diagnosis-treatment"], "sources": ["samhsa-treatment", "asam", "indiana"], "grove": ("Explore The Grove Estate's residential rehab program", "https://grovetreatment.com/programs/rehab/")
    },
    {
        "slug": "outpatient-rehab", "cluster": "Treatment guides", "title": "Outpatient Rehab in Indiana", "description": "Compare outpatient, intensive outpatient, and high-intensity outpatient addiction treatment in Indiana.",
        "answer": "Outpatient rehab provides scheduled addiction treatment without an overnight stay. Programs range from lower-intensity therapy and medication visits to intensive or high-intensity schedules, and some medically managed outpatient levels can address defined monitoring needs.",
        "facts": [("Outpatient is a broad category", "Visit frequency, hours, therapies, testing, medical services, and psychiatric capability vary."), ("Home stability matters", "Transportation, housing, substance exposure, safety, and support can affect whether outpatient care is workable."), ("Medication continuity can be central", "Ask how prescriptions, lab work, and follow-up are coordinated."), ("Step-down care should be specific", "Residential discharge plans should name the outpatient provider, appointment timing, and medication handoff.")],
        "questions": ["How many clinical hours and visits are expected each week?", "What happens if symptoms or use escalate between visits?", "Which medical, psychiatric, and medication services are on site?"],
        "faqs": [("Can outpatient rehab work around employment?", "Some programs offer flexible schedules, but clinical needs and attendance requirements come first."), ("Is IOP the same everywhere?", "No. Confirm hours, services, staffing, population, and the licensed level at the location."), ("Can outpatient care follow detox?", "Yes when clinically appropriate and safely coordinated."), ("Does outpatient treatment include drug testing?", "Many programs use testing as one clinical tool. Ask how results affect care and whether costs are included.")],
        "related": ["inpatient-rehab", "dual-diagnosis-treatment", "relapse-prevention", "rehab-cost", "insurance-for-rehab", "how-long-is-rehab"], "sources": ["samhsa-treatment", "asam", "indiana"], "grove": ("Review The Grove Estate's aftercare approach", "https://grovetreatment.com/programs/aftercare/")
    },
    {
        "slug": "dual-diagnosis-treatment", "cluster": "Treatment guides", "title": "Dual Diagnosis Treatment in Indiana", "description": "Learn how co-occurring substance-use and mental-health treatment works and what to verify in Indiana.",
        "answer": "Dual diagnosis treatment, also called co-occurring disorder treatment, addresses substance-use needs and mental-health conditions together or through closely coordinated care. The phrase alone does not prove psychiatric staffing, medication capability, or an integrated treatment model.",
        "facts": [("Assessment should cover both areas", "Substance use, withdrawal, mood, anxiety, trauma, psychosis, cognition, medications, safety, and functioning can affect the plan."), ("Integration is specific", "Ask whether the same team treats both conditions and how records and decisions are coordinated."), ("Crisis capability varies", "A program may treat stable co-occurring conditions but transfer acute psychiatric or medical emergencies."), ("Continuity reduces gaps", "Prescriptions, therapy, primary care, psychiatry, and recovery support need a documented handoff.")],
        "questions": ["Which psychiatric professionals are available and how often?", "Which co-occurring conditions or acuity levels cannot be admitted?", "How are psychiatric medications continued after discharge?"],
        "faqs": [("Is dual diagnosis a specific diagnosis?", "No. It is a common term for co-occurring substance-use and mental-health conditions."), ("Does every rehab treat co-occurring disorders?", "Programs should assess them, but capability and integration vary substantially."), ("Can trauma be addressed during rehab?", "It may be addressed through trauma-informed care, but the timing and depth of trauma treatment should fit safety and stabilization."), ("What does COE mean in ASAM terminology?", "Co-Occurring Enhanced refers to enhanced capability for specified psychiatric and cognitive needs at certain ASAM levels.")],
        "related": ["drug-rehab", "inpatient-rehab", "outpatient-rehab", "family-support-addiction", "relapse-prevention", "rehab-admissions-process"], "sources": ["asam", "samhsa-treatment", "indiana"], "grove": ("View The Grove Estate's dual-diagnosis program", "https://grovetreatment.com/programs/dual-diagnosis/")
    },
    {
        "slug": "opioid-rehab", "cluster": "Substance guides", "title": "Opioid Rehab in Indiana", "description": "Understand opioid treatment, medications, detox, overdose prevention, and Indiana provider questions.",
        "answer": "Opioid rehab should address opioid use disorder as an ongoing health condition rather than only treating short-term withdrawal. Evidence-based care can include medications for opioid use disorder, counseling and behavioral therapies, overdose prevention, medical care, and recovery support.",
        "facts": [("Medication access matters", "Buprenorphine, methadone, and naltrexone are FDA-approved medications used for opioid use disorder in appropriate clinical plans."), ("Detox alone can leave risk", "Loss of tolerance after abstinence can increase overdose danger if opioid use resumes."), ("Fentanyl changes the environment", "Illicit opioid exposure may be unpredictable, making naloxone and overdose education important."), ("Continuity should be arranged", "Confirm the next prescriber, appointment, pharmacy, insurance plan, and bridge medication before discharge.")],
        "questions": ["Which opioid-use-disorder medications are available or continued?", "How is naloxone provided and overdose risk discussed?", "What is the plan if withdrawal or cravings persist?"],
        "faqs": [("Is medication replacing one drug with another?", "No. Approved medications are evidence-based treatments used under clinical supervision to reduce withdrawal, cravings, and other risks."), ("Is opioid detox required before medication?", "Not always. Medication choice and timing are clinical decisions."), ("Can residential rehab continue methadone or buprenorphine?", "Policies vary. Confirm before admission and do not assume a medication will be stopped or continued."), ("What should family keep available?", "Naloxone and knowledge of overdose response are important when opioid exposure is possible.")],
        "related": ["fentanyl-rehab", "heroin-rehab", "medical-detox", "inpatient-rehab", "dual-diagnosis-treatment", "relapse-prevention"], "sources": ["samhsa-moud", "asam", "indiana"], "grove": ("View The Grove Estate's medical detox program", "https://grovetreatment.com/programs/detox/")
    },
    {
        "slug": "fentanyl-rehab", "cluster": "Substance guides", "title": "Fentanyl Rehab in Indiana", "description": "Learn how fentanyl treatment relates to opioid care, withdrawal, medications, and overdose prevention.",
        "answer": "Fentanyl rehab is opioid use disorder treatment adapted to a person's fentanyl exposure, withdrawal pattern, overdose history, health, and co-occurring substance use. Treatment should include opioid-specific medication options and overdose prevention, not merely a branded detox protocol.",
        "facts": [("Exposure can be uncertain", "Illicit fentanyl may appear in products sold as other opioids or drugs, so a complete use history and testing context matter."), ("Overdose risk is central", "Naloxone access, response education, and safer transition planning should be addressed."), ("Withdrawal care is individualized", "Symptoms, timing, and medication initiation can vary; clinicians should guide the plan."), ("Retention matters", "Ongoing medication and support after discharge are critical practical questions.")],
        "questions": ["How does the program initiate or continue opioid medications?", "How are naloxone and overdose education handled at discharge?", "Can the center treat concurrent benzodiazepine, alcohol, or stimulant use?"],
        "faqs": [("Is fentanyl rehab different from opioid rehab?", "It falls within opioid treatment, but exposure pattern, potency, withdrawal experience, and overdose history can affect the plan."), ("Does fentanyl always require inpatient detox?", "Not automatically. A clinician should assess medical, psychiatric, substance, and environmental risks."), ("Can medications be used?", "Yes. FDA-approved medications for opioid use disorder may be part of care."), ("Why is follow-up urgent?", "Overdose risk can remain high, especially after tolerance changes or treatment interruption.")],
        "related": ["opioid-rehab", "heroin-rehab", "medical-detox", "benzo-rehab", "dual-diagnosis-treatment", "family-support-addiction"], "sources": ["samhsa-moud", "asam", "indiana"], "grove": ("View The Grove Estate's medical detox program", "https://grovetreatment.com/programs/detox/")
    },
    {
        "slug": "heroin-rehab", "cluster": "Substance guides", "title": "Heroin Rehab in Indiana", "description": "Understand heroin treatment, medications for opioid use disorder, overdose prevention, and continuing care.",
        "answer": "Heroin rehab is treatment for opioid use disorder associated with heroin use. Effective planning can include medications for opioid use disorder, withdrawal support, counseling, overdose prevention, infectious-disease and medical care, and long-term recovery services.",
        "facts": [("Medication is a core option", "Ask whether buprenorphine, methadone, or naltrexone is offered, continued, or coordinated."), ("Street supply may include fentanyl", "The actual opioid exposure may be uncertain, changing overdose and withdrawal considerations."), ("Health screening can matter", "Injection-related infections, wounds, hepatitis, HIV risk, pain, and other medical needs may require care."), ("Transitions are high-risk moments", "Confirm medication continuity, naloxone, appointments, housing, and transportation before discharge.")],
        "questions": ["Which opioid medications can be started or continued?", "How are infection and other medical concerns evaluated?", "What concrete services begin immediately after discharge?"],
        "faqs": [("Is heroin withdrawal usually life-threatening?", "It is often extremely uncomfortable and can create complications, but risk depends on the whole clinical picture and other substances."), ("Can treatment begin without completing detox?", "Often, opioid medications can be initiated without a traditional abstinence-only detox sequence; clinicians determine timing."), ("What if fentanyl is also involved?", "Tell the clinical team about all known or possible exposure because it may affect assessment and medication planning."), ("Is naloxone still needed after rehab?", "Yes when opioid exposure remains possible; reduced tolerance can increase overdose risk.")],
        "related": ["opioid-rehab", "fentanyl-rehab", "medical-detox", "inpatient-rehab", "relapse-prevention", "family-support-addiction"], "sources": ["samhsa-moud", "asam", "indiana"], "grove": ("View The Grove Estate's medical detox program", "https://grovetreatment.com/programs/detox/")
    },
    {
        "slug": "cocaine-rehab", "cluster": "Substance guides", "title": "Cocaine Rehab in Indiana", "description": "Learn how cocaine treatment addresses stimulant use, medical and mental health risks, and recovery planning.",
        "answer": "Cocaine rehab is treatment for problematic cocaine or stimulant use. Care commonly emphasizes behavioral treatment, assessment of cardiovascular and psychiatric symptoms, sleep and nutrition recovery, co-occurring substance use, and a practical continuing-care plan.",
        "facts": [("Assessment should be broad", "Chest symptoms, blood pressure, sleep loss, mood, psychosis, suicidality, and other substances can affect urgency and placement."), ("Withdrawal differs from alcohol or sedatives", "Fatigue, sleep changes, mood symptoms, and cravings may require support even without the same medication protocol."), ("Behavioral care is important", "Ask which evidence-based behavioral approaches are delivered and by whom."), ("Polysubstance risk is common", "Possible fentanyl contamination or combined alcohol, opioid, or sedative use should be disclosed.")],
        "questions": ["How are acute cardiac or psychiatric symptoms screened?", "Which behavioral treatments are actually delivered?", "How does the program address cravings and return-to-use risk after discharge?"],
        "faqs": [("Is there a standard detox medication for cocaine?", "There is no single universally used detox medication equivalent to opioid-use-disorder medications; treatment is individualized."), ("Can cocaine withdrawal affect mood?", "Yes. Depression, anxiety, sleep changes, and suicidal thoughts require clinical attention."), ("Does cocaine use require residential care?", "Not automatically. Assessment should determine the appropriate setting and intensity."), ("What if cocaine may contain fentanyl?", "Discuss possible exposure and overdose prevention, including naloxone.")],
        "related": ["meth-rehab", "drug-rehab", "dual-diagnosis-treatment", "outpatient-rehab", "inpatient-rehab", "relapse-prevention"], "sources": ["samhsa-treatment", "asam", "indiana"], "grove": ("Explore The Grove Estate's residential rehab program", "https://grovetreatment.com/programs/rehab/")
    },
    {
        "slug": "meth-rehab", "cluster": "Substance guides", "title": "Meth Rehab in Indiana", "description": "Understand methamphetamine treatment, psychiatric and medical assessment, behavioral care, and continuing support.",
        "answer": "Meth rehab is treatment for methamphetamine or stimulant use disorder. A careful plan addresses sleep deprivation, mood, psychosis, cardiovascular and dental health, nutrition, other substances, behavioral treatment, and the recovery environment.",
        "facts": [("Acute symptoms may need urgent care", "Severe agitation, chest pain, psychosis, suicidality, overheating, or collapse require emergency evaluation."), ("Sleep and mood can take time", "Early recovery may involve fatigue, disrupted sleep, low mood, anxiety, and cravings."), ("Behavioral treatment should be concrete", "Ask which structured interventions are offered and how progress is measured."), ("Environment affects return risk", "Housing, relationships, transportation, work, and access to recovery support belong in the plan.")],
        "questions": ["How does the program evaluate psychosis, depression, and suicide risk?", "Which evidence-based behavioral services are provided?", "What continuing support is arranged for the first week after discharge?"],
        "faqs": [("Is meth withdrawal medically dangerous?", "Risks vary. Psychiatric symptoms, exhaustion, other substances, and medical conditions can require close or urgent care."), ("Is there an approved medication specifically for meth use disorder?", "Treatment commonly relies on behavioral care and individualized medical or psychiatric management; ask about current evidence-based options."), ("Can sleep be restored immediately?", "Sleep and energy may recover gradually and should be monitored with mood and safety."), ("Can outpatient treatment help?", "Yes for some people when clinical needs, safety, and recovery environment support it.")],
        "related": ["cocaine-rehab", "drug-rehab", "dual-diagnosis-treatment", "inpatient-rehab", "outpatient-rehab", "family-support-addiction"], "sources": ["samhsa-treatment", "asam", "indiana"], "grove": ("Explore The Grove Estate's residential rehab program", "https://grovetreatment.com/programs/rehab/")
    },
    {
        "slug": "benzo-rehab", "cluster": "Substance guides", "title": "Benzodiazepine Rehab in Indiana", "description": "Learn why benzodiazepine withdrawal needs clinical planning and how to compare Indiana treatment capabilities.",
        "answer": "Benzodiazepine rehab may involve a clinician-directed taper, monitored withdrawal management, treatment for benzodiazepine use disorder, and care for the condition the medication was treating. People who may be physically dependent should not stop abruptly without clinical guidance.",
        "facts": [("Dependence is not identical to addiction", "Physical dependence can occur with prescribed use; assessment should distinguish it from a substance use disorder."), ("Abrupt stopping can be dangerous", "Seizures and other severe withdrawal complications are possible."), ("Tapers are individualized", "Dose, duration, medication, age, health, symptoms, and other substances affect planning."), ("Co-use changes risk", "Alcohol and opioids can increase overdose or withdrawal complexity and must be disclosed.")],
        "questions": ["Who designs, prescribes, and adjusts the taper?", "How are seizures and severe withdrawal risks managed?", "How are anxiety, insomnia, pain, or other underlying conditions treated?"],
        "faqs": [("Should benzodiazepines be stopped suddenly?", "Not when physical dependence may be present. ASAM guidance advises gradual, supervised tapering rather than abrupt discontinuation."), ("How long does a taper take?", "It varies widely and may take months or longer depending on the individual."), ("Is residential treatment always required?", "No. The setting should follow risk, symptoms, co-use, health, support, and ability to follow a taper safely."), ("What if opioids are also used?", "Tell the clinician. Combined use raises overdose risk and may require naloxone and coordinated treatment.")],
        "related": ["medical-detox", "alcohol-detox", "dual-diagnosis-treatment", "inpatient-rehab", "outpatient-rehab", "rehab-admissions-process"], "sources": ["asam-benzo", "asam", "indiana"], "grove": ("View The Grove Estate's medical detox program", "https://grovetreatment.com/programs/detox/")
    },
    {
        "slug": "rehab-cost", "cluster": "Planning guides", "title": "How Much Does Rehab Cost in Indiana?", "description": "Understand the factors that shape rehab cost and how to request a transparent written estimate in Indiana.",
        "answer": "Rehab cost in Indiana varies by level of care, length, medical and psychiatric services, medications, room type, insurance contract, and provider. A useful comparison starts with a written estimate for the exact location and proposed level, not a generic daily price.",
        "facts": [("Clinical intensity affects cost", "Hospital, medically managed, residential, intensive outpatient, and standard outpatient services use different resources."), ("Insurance changes the calculation", "Deductible, coinsurance, copays, network status, authorization, and medical necessity all matter."), ("Extra charges should be named", "Ask about labs, medications, physician services, transportation, testing, room upgrades, and outside appointments."), ("Cheapest is not automatically best fit", "The program still needs to safely meet substance, withdrawal, medical, psychiatric, and recovery needs.")],
        "questions": ["Can I receive an itemized written estimate before admission?", "Which services may be billed separately or by outside clinicians?", "What are the deposit, cancellation, transfer, and refund terms?"],
        "faqs": [("Can a center guarantee my final cost?", "Usually not before benefits and clinical needs are confirmed, but it should explain assumptions and likely patient responsibility."), ("Does insurance cover room upgrades?", "Often not. Ask which room is clinically covered and the private-pay difference."), ("Can costs change during treatment?", "Yes if level, duration, medications, or services change. Ask how consent and estimates are updated."), ("Should I pay before benefits are verified?", "Understand the written terms, network status, authorization process, and refund policy first.")],
        "related": ["insurance-for-rehab", "rehab-admissions-process", "how-long-is-rehab", "inpatient-rehab", "outpatient-rehab", "what-to-pack-for-rehab"], "sources": ["niaaa-quality", "medicare", "indiana"], "grove": ("Review The Grove Estate's program information", "https://grovetreatment.com/")
    },
    {
        "slug": "insurance-for-rehab", "cluster": "Planning guides", "title": "Insurance for Rehab in Indiana", "description": "Learn how to verify rehab benefits, network status, authorization, and patient responsibility in Indiana.",
        "answer": "Insurance coverage for rehab depends on the plan, provider network, diagnosis, medical necessity, authorization, level of care, and services delivered. A benefits check is not a guarantee of payment, so request both insurer confirmation and a provider estimate.",
        "facts": [("Network status is location-specific", "A provider brand may have different contracts by facility, clinician, or service."), ("Authorization may be required", "Ask who submits clinical information and what happens if days or levels are denied."), ("Benefits are not final claims", "Deductibles, coinsurance, exclusions, coding, and changing clinical needs can affect responsibility."), ("Appeal rights may exist", "Ask the insurer and provider for written denial reasons and appeal procedures.")],
        "questions": ["Is this exact facility and level in network?", "What authorization and continued-stay reviews are required?", "What is the estimated patient responsibility and what is excluded?"],
        "faqs": [("Does accepting insurance mean in network?", "No. A provider may bill a plan without having an in-network contract."), ("What information should I get from the insurer?", "Record representative, date, reference number, network status, benefits, deductible, coinsurance, authorization, and exclusions."), ("Can rehab be denied as not medically necessary?", "Coverage decisions can depend on plan criteria and clinical documentation. Ask about review and appeal steps."), ("Does Medicare cover substance-use treatment?", "Medicare covers certain mental health and substance-use services when requirements are met; confirm the provider and service.")],
        "related": ["rehab-cost", "rehab-admissions-process", "inpatient-rehab", "outpatient-rehab", "how-long-is-rehab", "medical-detox"], "sources": ["medicare", "niaaa-quality", "indiana"], "grove": ("Contact The Grove Estate through its official website", "https://grovetreatment.com/")
    },
    {
        "slug": "rehab-admissions-process", "cluster": "Planning guides", "title": "Rehab Admissions Process in Indiana", "description": "Prepare for rehab admission, pre-assessment, benefits review, travel, medications, and arrival in Indiana.",
        "answer": "Rehab admission usually includes an initial call, clinical pre-assessment, medical and substance-use history, benefits or payment review, suitability decision, arrival planning, and an in-person evaluation. Admission is not final until the program confirms it can safely provide the needed care.",
        "facts": [("Be complete and accurate", "Disclose substances, last use, withdrawal history, health conditions, pregnancy, psychiatric symptoms, medications, allergies, and recent emergencies."), ("Phone screening has limits", "The level or location may change after an in-person assessment."), ("Payment and clinical approval are separate", "Insurance verification does not establish suitability, and clinical acceptance does not guarantee coverage."), ("Arrival details prevent delays", "Confirm timing, transportation, belongings, medication handling, identification, communication, and emergency instructions.")],
        "questions": ["Who makes the final clinical acceptance decision?", "What could trigger hospital evaluation or a different placement?", "What should be brought, left home, or sent in advance?"],
        "faqs": [("How quickly can admission happen?", "It depends on clinical review, bed availability, payment, transportation, and whether emergency stabilization is needed."), ("Can family complete admission for someone?", "Family can provide information and support, but consent and admission requirements still apply except under specific legal circumstances."), ("Will prescribed medication be allowed?", "The clinical team must review it. Bring accurate medication information and follow packing instructions."), ("What if symptoms worsen before arrival?", "Contact emergency services or an appropriate medical setting rather than continuing travel to a non-emergency facility.")],
        "related": ["what-to-pack-for-rehab", "insurance-for-rehab", "rehab-cost", "medical-detox", "how-long-is-rehab", "family-support-addiction"], "sources": ["samhsa-treatment", "asam", "indiana"], "grove": ("Review The Grove Estate's official programs", "https://grovetreatment.com/programs/")
    },
    {
        "slug": "how-long-is-rehab", "cluster": "Planning guides", "title": "How Long Is Rehab?", "description": "Understand what affects detox, residential, and outpatient treatment length and how to plan transitions.",
        "answer": "There is no single correct rehab length. Duration depends on withdrawal risk, diagnosis, medical and psychiatric needs, progress, recovery environment, level of care, coverage, and the availability of a safe next step.",
        "facts": [("Detox timing is individualized", "Substance, use pattern, symptoms, medications, health, and response affect stabilization."), ("A advertised program length is not a clinical rule", "Thirty-, sixty-, or ninety-day labels can describe packaging, but reassessment should guide care."), ("Continuum matters more than one stay", "Treatment may move across residential, intensive outpatient, standard outpatient, medications, and recovery support."), ("Early discharge needs a plan", "Ask how the program handles coverage limits, patient choice, transfer, and discharge against advice.")],
        "questions": ["How often is continued need and level of care reassessed?", "What clinical milestones guide transition rather than a calendar date?", "What services and appointments are confirmed before discharge?"],
        "faqs": [("Is 30 days enough?", "It may be one phase for some people, but need and continuity matter more than a universal number."), ("Can insurance limit length?", "Coverage decisions can affect authorized days; ask how reviews and appeals are handled."), ("Can rehab be extended?", "Potentially, based on clinical need, program capability, availability, and payment."), ("Does longer always mean better?", "No. Care should be appropriate, effective, reassessed, and connected to the next level.")],
        "related": ["inpatient-rehab", "outpatient-rehab", "medical-detox", "rehab-cost", "insurance-for-rehab", "relapse-prevention"], "sources": ["asam", "samhsa-treatment", "niaaa-quality"], "grove": ("Review The Grove Estate's continuing-care approach", "https://grovetreatment.com/programs/aftercare/")
    },
    {
        "slug": "what-to-pack-for-rehab", "cluster": "Planning guides", "title": "What to Pack for Rehab", "description": "Use a verification-first packing checklist for detox or residential rehab admission in Indiana.",
        "answer": "Pack only after receiving the facility's current written list because medication, clothing, device, tobacco, food, and personal-item policies vary. Essentials often include identification, insurance information, approved medications, emergency contacts, and practical clothing.",
        "facts": [("Medication needs special handling", "Bring an accurate list and follow instructions about original pharmacy containers; do not assume all prescriptions or supplements are allowed."), ("Devices may be restricted", "Phone, laptop, charger, camera, and internet policies can change by clinical phase or professional track."), ("Safety rules are specific", "Razors, cords, aerosols, glass, outside food, nicotine products, and valuables may be prohibited or secured."), ("Label practical items", "Use the facility's rules for quantities, laundry, toiletries, bedding, and storage.")],
        "questions": ["Can you send the current written packing and prohibited-item list?", "How should prescribed medications and controlled substances arrive?", "What happens to cash, cards, valuables, and prohibited items?"],
        "faqs": [("Can I bring my phone?", "Policies vary. Confirm whether it is stored, permitted on a schedule, or allowed after stabilization."), ("Can I bring toiletries?", "Often with restrictions on alcohol content, aerosols, glass, or opened products."), ("Should I bring bedding?", "Usually facilities provide it, but confirm."), ("Can family deliver items later?", "Often only after staff inspection and according to delivery rules.")],
        "related": ["rehab-admissions-process", "inpatient-rehab", "medical-detox", "how-long-is-rehab", "family-support-addiction", "rehab-cost"], "sources": ["samhsa-treatment", "indiana"], "grove": ("Confirm The Grove Estate's current admission policies", "https://grovetreatment.com/")
    },
    {
        "slug": "family-support-addiction", "cluster": "Family and recovery", "title": "Family Support for Addiction", "description": "Learn how families can support treatment, communicate concerns, protect safety, and care for themselves.",
        "answer": "Family support can help a person connect with and remain engaged in treatment, but family members cannot control another person's recovery. Useful support combines compassion, clear safety boundaries, accurate information, professional guidance, and care for the family's own health.",
        "facts": [("Start with concern, not confrontation", "Describe specific changes and safety concerns without labels, threats, or shame."), ("Prepare practical help", "Offer to research providers, join a call with consent, arrange transportation, care for dependents, or locate naloxone."), ("Protect immediate safety", "Call 911 for overdose, severe withdrawal, violence, collapse, or imminent danger; call or text 988 for a suicide or mental-health crisis."), ("Family members need support too", "Counseling, family therapy, peer groups, and respite can reduce isolation and burnout.")],
        "questions": ["What information can the program receive from family even without a release?", "How are updates and family sessions handled with consent?", "What boundaries and emergency plan should the household use?"],
        "faqs": [("Can I force an adult into rehab?", "Laws and emergency standards are specific. Seek qualified legal or crisis guidance rather than relying on general internet advice."), ("Should I give money to help?", "Consider whether help supports safety and treatment or unintentionally supports continued use; professional guidance can help set boundaries."), ("Can family contact the clinical team?", "You can usually provide information, but the team may be unable to disclose information without consent."), ("What if my loved one refuses help?", "Keep communication open, maintain safety boundaries, seek support, and be ready with verified options if willingness changes.")],
        "related": ["rehab-admissions-process", "relapse-prevention", "dual-diagnosis-treatment", "opioid-rehab", "signs-someone-needs-rehab", "helping-a-loved-one-enter-rehab"], "sources": ["samhsa-family", "samhsa-recovery", "indiana"], "grove": ("View The Grove Estate's family integration program", "https://grovetreatment.com/programs/family/")
    },
    {
        "slug": "relapse-prevention", "cluster": "Family and recovery", "title": "Relapse Prevention and Continuing Care", "description": "Build a practical continuing-care plan for triggers, medications, support, and rapid re-engagement.",
        "answer": "Relapse prevention is an individualized plan for recognizing risk, using coping and support strategies, continuing treatment, and responding quickly if substance use returns. A return to use is a safety and treatment signal, not proof that recovery is impossible.",
        "facts": [("Plan before discharge", "Appointments, prescriptions, transportation, housing, contacts, and crisis steps should be concrete."), ("Triggers are not only places", "Stress, pain, sleep, conflict, isolation, mental health symptoms, medication gaps, and exposure can raise risk."), ("Overdose risk can change", "Reduced tolerance after abstinence can increase danger, especially with opioids."), ("Rapid re-engagement matters", "The plan should say who to contact and where to go without shame or delay.")],
        "questions": ["What appointments and medications are confirmed before discharge?", "How are early warning signs and high-risk situations documented?", "What is the same-day response if use or cravings escalate?"],
        "faqs": [("Does relapse mean treatment failed?", "No. It indicates that safety and the treatment plan need reassessment."), ("What belongs in a prevention plan?", "Warning signs, coping tools, people to contact, medication plan, meetings or therapy, naloxone when relevant, and rapid-care options."), ("Can family help with the plan?", "Yes with consent and healthy boundaries."), ("Is aftercare only support groups?", "No. It may include medical care, medication, therapy, outpatient treatment, peer support, recovery housing, and monitoring.")],
        "related": ["family-support-addiction", "outpatient-rehab", "dual-diagnosis-treatment", "how-long-is-rehab", "opioid-rehab", "alcohol-rehab"], "sources": ["samhsa-recovery", "asam", "niaaa-quality"], "grove": ("View The Grove Estate's aftercare program", "https://grovetreatment.com/programs/aftercare/")
    },
    {
        "slug": "signs-someone-needs-rehab", "cluster": "Family and recovery", "title": "Signs Someone May Need Addiction Treatment", "description": "Recognize patterns that support professional assessment without trying to diagnose a loved one online.",
        "answer": "Someone may need a professional substance-use assessment when alcohol or drug use is causing loss of control, withdrawal, hazardous behavior, health problems, relationship or work disruption, repeated unsuccessful attempts to change, or continued use despite harm. Only a qualified professional can diagnose and recommend a level of care.",
        "facts": [("Look for patterns, not one stereotype", "Changes in functioning, safety, health, finances, sleep, mood, and relationships may be relevant."), ("Withdrawal or overdose raises urgency", "Seizures, severe confusion, breathing problems, unconsciousness, or imminent danger require emergency help."), ("Mental health can overlap", "Depression, anxiety, trauma, psychosis, and suicide risk need direct assessment."), ("Conversation should preserve dignity", "Use specific observations, concern, and an offer of practical help rather than labels or public confrontation.")],
        "questions": ["What specific changes and safety events have occurred?", "Is there current intoxication, withdrawal, overdose, or suicide risk?", "Which professional can complete a timely assessment?"],
        "faqs": [("Do they have to hit bottom?", "No. Earlier assessment and support may reduce harm."), ("Can I diagnose addiction from a checklist?", "No. Checklists can prompt concern, but diagnosis requires professional assessment."), ("What if the person is in immediate danger?", "Call 911. For suicide or mental-health crisis support, call or text 988."), ("How do I raise the subject?", "Choose a calm time, describe specific observations, listen, avoid shame, and offer a verified next step.")],
        "related": ["helping-a-loved-one-enter-rehab", "family-support-addiction", "rehab-admissions-process", "medical-detox", "dual-diagnosis-treatment", "drug-rehab"], "sources": ["samhsa-family", "samhsa-treatment", "indiana"], "grove": ("Review The Grove Estate's official program options", "https://grovetreatment.com/programs/")
    },
    {
        "slug": "helping-a-loved-one-enter-rehab", "cluster": "Family and recovery", "title": "Helping a Loved One Enter Rehab", "description": "Prepare a respectful conversation, verified options, practical admission help, and an emergency plan.",
        "answer": "Helping a loved one enter rehab works best when concern is specific, options are verified, practical barriers are addressed, and the person is treated with dignity. Prepare for both a treatment conversation and the possibility that the person is not ready immediately.",
        "facts": [("Research before the conversation", "Verify location, clinical fit, availability, payment, transportation, and what happens if detox or hospital evaluation is needed."), ("Use concrete observations", "Speak about events and safety rather than arguing over labels."), ("Offer choices and practical support", "A person may engage more readily when offered qualified options and help with calls, travel, work, children, or pets."), ("Boundaries should be safe and sustainable", "Family support does not require financing use, accepting violence, or hiding emergencies.")],
        "questions": ["Which two or three verified options fit the current clinical needs?", "What practical barrier can the family safely help solve?", "What is the emergency plan if overdose, withdrawal, or violence occurs?"],
        "faqs": [("Should the family stage an intervention?", "Some families use trained professionals, but confrontational or poorly planned approaches can backfire. Seek qualified guidance."), ("Can I call admissions without the person?", "You can ask general questions and provide information, but consent is usually needed for personal disclosure and voluntary admission."), ("What if they agree and then change their mind?", "Keep the next step simple, reduce delay, preserve dignity, and maintain safety boundaries."), ("What if they need detox first?", "The receiving program should assess withdrawal risk and direct the person to the appropriate setting.")],
        "related": ["family-support-addiction", "signs-someone-needs-rehab", "rehab-admissions-process", "what-to-pack-for-rehab", "medical-detox", "insurance-for-rehab"], "sources": ["samhsa-family", "samhsa-treatment", "indiana"], "grove": ("View The Grove Estate's family integration program", "https://grovetreatment.com/programs/family/")
    }
]

TITLE_BY_SLUG = {topic["slug"]: topic["title"] for topic in TOPICS}


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def render(topic: dict) -> str:
    slug = topic["slug"]
    canonical = f"{BASE}{slug}/"
    citations = [SOURCES[key] for key in topic["sources"]]
    image = CLUSTER_IMAGES[topic["cluster"]]
    image_url = f"{BASE}assets/topic-images/{image['file']}"
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "MedicalWebPage",
                "@id": f"{canonical}#page",
                "url": canonical,
                "name": topic["title"],
                "description": topic["description"],
                "dateModified": "2026-08-19",
                "lastReviewed": "2026-08-19",
                "isPartOf": {"@id": f"{BASE}#website"},
                "breadcrumb": {"@id": f"{canonical}#breadcrumb"},
                "citation": [url for _, url in citations],
                "primaryImageOfPage": {"@id": f"{canonical}#primaryimage"},
            },
            {
                "@type": "ImageObject",
                "@id": f"{canonical}#primaryimage",
                "contentUrl": image_url,
                "url": image_url,
                "width": 1536,
                "height": 1024,
                "caption": image["caption"],
                "representativeOfPage": True,
                "creditText": "Indiana Detox Guide",
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{canonical}#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Indiana Detox Guide", "item": BASE},
                    {"@type": "ListItem", "position": 2, "name": topic["title"], "item": canonical},
                ],
            },
        ],
    }
    facts = "".join(f'<li><strong>{esc(title)}</strong>{esc(body)}</li>' for title, body in topic["facts"])
    questions = "".join(f'<article class="topic-question">{esc(q)}</article>' for q in topic["questions"])
    faqs = "".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in topic["faqs"])
    related = "".join(f'<li><a href="../{slug2}/">{esc(TITLE_BY_SLUG[slug2])}</a></li>' for slug2 in topic["related"][:3])
    sources = "".join(f'<li><a href="{esc(url)}" target="_blank" rel="noreferrer">{esc(name)}</a></li>' for name, url in citations)
    grove_label, grove_url = topic["grove"]
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{esc(topic["title"])} | Indiana Detox Guide</title>
    <meta name="description" content="{esc(topic["description"])}" />
    <link rel="canonical" href="{canonical}" />
    <link rel="stylesheet" href="../tokens.css" />
    <link rel="stylesheet" href="../styles.css" />
    <link rel="stylesheet" href="../topic-pages.css" />
    <script type="application/ld+json">{json.dumps(schema, separators=(",", ":"))}</script>
  </head>
  <body>
    <header class="site-header"><a class="brand" href="../"><span class="brand-mark">ID</span><span>Indiana Detox Guide</span></a><nav class="main-nav" aria-label="Main navigation"><a href="../#faq">FAQs</a><a href="../#shortlist">Centers</a><a href="../#method">Method</a></nav></header>
    <main>
      <section class="topic-hero"><div class="topic-hero-inner"><p class="breadcrumb"><a href="../">Guide</a> / {esc(topic["cluster"])}</p><div class="topic-hero-grid"><div class="topic-hero-copy"><p class="section-kicker">Indiana treatment education</p><h1>{esc(topic["title"])}</h1><p class="topic-lede">{esc(topic["answer"])}</p><p class="topic-meta"><span>Reviewed {REVIEWED}</span><span>Educational resource</span><span>Indiana scope</span></p><div class="profile-actions"><a class="button button-primary" href="../#shortlist">Compare Indiana centers</a><a class="button button-light" href="{esc(grove_url)}" target="_blank" rel="noreferrer">{esc(grove_label)}</a></div></div><figure class="topic-hero-figure"><img src="../assets/topic-images/{esc(image['file'])}" width="1536" height="1024" alt="{esc(image['alt'])}" decoding="async" fetchpriority="high" /><figcaption>{esc(image['caption'])}</figcaption></figure></div></div></section>
      <section class="topic-section"><div class="topic-layout"><div><p class="section-kicker">Decision points</p><h2>What matters before choosing care</h2><ul class="topic-facts">{facts}</ul></div><aside class="topic-aside"><p class="section-kicker">Featured example</p><h2>The Grove Estate</h2><p>The guide features The Grove Estate as a private-retreat example. This is an editorial distinction, not a clinical outcome ranking. Verify current services and suitability directly.</p><a href="../centers/the-grove-estate/">Read the guide profile</a></aside></div></section>
      <section class="topic-section"><p class="section-kicker">Admissions call</p><h2>Questions to ask</h2><div class="topic-questions">{questions}</div></section>
      <section class="topic-section topic-faq"><p class="section-kicker">Common questions</p><h2>{esc(topic["title"])} FAQs</h2>{faqs}</section>
      <section class="topic-section"><div class="topic-layout"><div><p class="section-kicker">Continue researching</p><h2>Related Indiana guides</h2><ul class="topic-related">{related}</ul></div><aside class="topic-aside"><h2>Authoritative sources</h2><ul class="topic-sources">{sources}</ul><p class="source-note">Sources support general education. They do not verify a listed provider's current services.</p></aside></div></section>
      <section class="topic-section topic-notice"><p class="section-kicker">Safety note</p><h2>Information is not a clinical assessment</h2><p>This guide cannot determine diagnosis, withdrawal risk, or level of care. Call 911 for overdose, seizures, severe confusion, breathing problems, collapse, violence, or immediate danger. Call or text 988 for suicide or mental-health crisis support.</p><p class="source-note">Confirm credentials, staffing, insurance, services, and admission suitability directly with the exact Indiana location.</p></section>
    </main>
    <footer class="site-footer"><p>Independent Indiana treatment education. Information, not medical advice.</p><nav class="footer-links" aria-label="Discovery"><a href="../">Guide home</a></nav></footer>
  </body>
</html>'''


def main() -> None:
    for topic in TOPICS:
        folder = ROOT / topic["slug"]
        folder.mkdir(exist_ok=True)
        (folder / "index.html").write_text(render(topic), encoding="utf-8", newline="\n")
    print(f"Generated {len(TOPICS)} topic pages.")


if __name__ == "__main__":
    main()
