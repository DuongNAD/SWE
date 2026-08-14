#!/usr/bin/env python3
"""Rewrite tất cả hook trong meo.json sang format tiếng Anh:
   <English stem keyword> → <English answer keywords>

Bước 1: Chuẩn hoá '->' thành '→'
Bước 2: Rewrite 58 hook có tiếng Việt bằng mapping thủ công.
Bước 3: Ghi lại meo.json + chạy build.py
"""
import json, os, re, copy

SP = os.path.dirname(os.path.abspath(__file__))
MEO_PATH = os.path.join(SP, "meo.json")
CAU_HOI_PATH = "/Users/duongnad/Documents/project/SWE/05_quiz/cau_hoi.json"

# Load
meo = json.load(open(MEO_PATH))
cau_hoi_data = json.load(open(CAU_HOI_PATH))
cau_hoi = cau_hoi_data["cau_hoi"]

# Build slide -> question index
slide_map = {}
for i, q in enumerate(cau_hoi):
    slide_map[str(q["slide"])] = q

VIET_CHARS = set('àáảãạăắằẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđÀÁẢÃẠĂẮẰẴẶÂẤẦẨẪẬÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴĐ')

def has_viet(s):
    return any(c in VIET_CHARS for c in s)

# ===== MANUAL REWRITES for Vietnamese hooks =====
# Key = slide number (string), Value = new moc_nho in English
MANUAL = {
    "9":   "test case effectiveness → code coverage, outcomes, execution time",
    "20":  "use case extension → Condition, Event, Exception",
    "21":  "validating requirements → Peer review, Traceability, Automated tools",
    "44":  "risk impact → consequences on milestones",
    "62":  "design patterns NOT → NOT described using program code",
    "65":  "configuration management NOT → NOT risk management",
    "67":  "Four P's NOT → NOT plan",
    "97":  "Amazon Q Developer → Code generation, Explaining code",
    "101": "trained model → predictions without instructions, mimic human",
    "102": "Amazon Q Developer Java → suggestions, errors, optimization",
    "109": "AI code review → inefficiencies, coding standards, security",
    "111": "Generative AI → painting from prompt, writing stories, completing code",
    "125": "Random Forests → reduced overfitting, versatility, accuracy",
    "153": "Random Forest prediction → average of individual predictions",
    "164": "SEI-CMM and PCMM → assess and improve practices",
    "169": "source code changed → regression testing",
    "180": "GenAI code review → automating bug identification",
    "189": "nested loop testing → inner first, outer at minimum",
    "190": "AI refactoring → identifying simplification opportunities",
    "191": "GenAI code review → automating detection of inefficiencies",
    "192": "Amazon Q prompt → describe in natural language",
    "196": "Amazon Q explain → breaks code into smaller parts",
    "197": "few-shot prompting → providing a few examples",
    "199": "decision tree new data → overfitting, too many splits",
    "204": "interface abstraction → understanding the system",
    "209": "reviews/inspections → Yes, both detect faults",
    "210": "defensive programming → not let input crash program",
    "211": "quality design goals → reducing complexity of designing",
    "212": "two classes → yes, multiple associations always possible",
    "223": "cyclomatic complexity → safety, error free",
    "227": "statement coverage → No, does NOT guarantee all defects found",
    "231": "verbose switch → replace with enum",
    "232": "synchronized blocks → redundant synchronization",
    "233": "AI documentation → auto-generate and maintain docs",
    "234": "GenAI code review → identify errors, improve quality",
    "236": "deepfake → fraud, misinformation",
    "237": "Generative vs Discriminative → creates new vs classifies existing",
    "238": "GitHub Copilot → auto-generating Java code",
    "239": "contextual prompt → includes background information",
    "242": "random forests → reduce overfitting, combining multiple trees",
    "248": "AI vs ML → ML is a subset of AI",
    "247": "software complexity NOT → NOT insufficient hardware",
    "245": "GitHub Copilot → generate code, debugging fixes, suggest functions",
    "253": "software process → easier to divide work among team",
    "254": "AI software design → boilerplate code, suggest design patterns",
    "255": "association NOT → NOT an instance of relationship",
    "256": "early test design FALSE → FALSE takes more effort",
    "259": "Amazon Q Developer → syntax error corrections, code snippets",
    "263": "digital transformation → data personalization, automation, training",
    "262": "AI explain decisions → SHAP feature contribution",
    "264": "XOR constraint → only one of two classes",
    "266": "entity class → persistent information",
    "267": "incomplete coverage → superclass not member of any subclass",
    "268": "requirements validation → use a checklist",
    "269": "cost of fixing fault → increases towards live use",
    "271": "Bridge pattern → decouple abstraction from implementation",
    "272": "6 hours, 80% attendance → Pass",
    "274": "use case class distribution → isolate changes to specific classes",
}

# Stats
fixed_arrow = 0
fixed_viet = 0
already_ok = 0
missing = 0

for slide_str, m in meo.items():
    old = m.get("moc_nho", "")

    # Step 1: Fix arrow
    if "->" in old and "→" not in old:
        old = old.replace("->", "→")
        fixed_arrow += 1

    # Step 2: Fix Vietnamese hooks
    if has_viet(old):
        if slide_str in MANUAL:
            m["moc_nho"] = MANUAL[slide_str]
            fixed_viet += 1
        else:
            # Flag missing
            print(f"⚠️  THIẾU MAPPING slide {slide_str}: {old}")
            missing += 1
    else:
        if slide_str not in MANUAL:
            # Already English — just make sure arrow is right
            m["moc_nho"] = old
            already_ok += 1
        else:
            # In manual but not Vietnamese? Override anyway
            m["moc_nho"] = MANUAL[slide_str]
            fixed_viet += 1

# Also check: any slides with Vietnamese in hooks that aren't in meo.json?
for q in cau_hoi:
    s = str(q["slide"])
    if s not in meo:
        print(f"⚠️  Slide {s} KHÔNG CÓ trong meo.json")

# Save
json.dump(meo, open(MEO_PATH, "w"), ensure_ascii=False, indent=2)

print(f"\n=== KẾT QUẢ ===")
print(f"Đã chuẩn hoá '→': {fixed_arrow}")
print(f"Đã rewrite tiếng Việt → tiếng Anh: {fixed_viet}")
print(f"Đã đúng format: {already_ok}")
print(f"Thiếu mapping: {missing}")
print(f"Tổng entries: {len(meo)}")
