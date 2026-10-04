<div align="center">

# TRITON OCEAN SYSTEMS

### Make the ocean observable.

**Ocean data. Distributed observation. Persistent intelligence.**

[View the live investor deck](https://triton-ocean-systems.github.io/investor-deck/index.html) · [Open the deck PDF](Triton_PreSeed_Deck_v4.pdf) · [Review claims and assumptions](CLAIMS_AND_ASSUMPTIONS.md)

</div>

---

## The investment thesis

Triton Ocean Systems is developing a distributed observation network designed to turn coastal and vessel observations into persistent, queryable ocean data.

The network and its data are the core product. Customer discovery determines which observations have commercial value, where new coverage is justified, and how access should be priced. Sargassum monitoring is one possible application; it does not define the company or require county procurement as the first route to market.

Triton's potential advantage depends on useful coverage, reliable delivery and a permissioned historical record. More nodes create value only when their observations improve a buyer's work or support economical reuse across customers.

## View the deck

**Live GitHub Pages presentation:** [triton-ocean-systems.github.io/investor-deck](https://triton-ocean-systems.github.io/investor-deck/index.html)

**Source repository:** [github.com/Triton-Ocean-Systems/investor-deck](https://github.com/Triton-Ocean-Systems/investor-deck)

| Resource | Purpose |
|---|---|
| [Live presentation](https://triton-ocean-systems.github.io/investor-deck/index.html) | Browser-based deck with a PDF download. Reflects the deployed branch. |
| [Network-first deck · v4](Triton_PreSeed_Deck_v4.pdf) | The 12-page investor narrative included with this source revision. |
| [Claims and assumptions](CLAIMS_AND_ASSUMPTIONS.md) | Evidence, sources, financial assumptions and tests that could disprove the thesis. |
| [Editable build source](build_deck.py) | Text, layout and presentation logic used to generate the PDF. |
| [Revision pull request](https://github.com/Triton-Ocean-Systems/investor-deck/pull/2) | Review the proposed deck and source changes before deployment. |

The live presentation may show an earlier version until the revision is merged and GitHub Pages finishes deployment. The PDF link above follows the files on the branch being viewed.

## What the deck covers

1. Triton's ocean data and observation-network positioning.
2. The economic burden of missing or difficult-to-use observations.
3. The proposed data product and observation architecture.
4. Node 001 validation from capture through delivery.
5. Buyer discovery and demand-guided deployment.
6. Recurring data access and coverage economics.
7. Bottom-up market scenarios based on qualified buying accounts.
8. Existing observation systems and commercial alternatives.
9. The conditions for a compounding data advantage.
10. Founder evidence and the current company stage.
11. Technical and commercial milestones over an 18-month planning horizon.
12. The proposed $1.2M pre-seed raise and capital allocation.

## Observation architecture

| Component | Intended role |
|---|---|
| **BeachNode** | Fixed coastal observation. |
| **SailNode** | Mobile development and field validation. |
| **Vessel integrations** | Observation inputs from third-party assets, subject to access and use rights. |
| **EdgeCore** | Local capture, processing and buffering when connectivity is interrupted. |
| **Triton data platform** | Proposed archive and query/API access with source and quality context. |

These are design roles, not a claim of a deployed fleet. Node 001's planned NMEA / AIS / GNSS inputs can validate a data path; they do not, by themselves, establish oceanographic measurement or commercial differentiation. Environmental datasets require suitable instrumentation and calibration.

## Current stage and evidence

The original deck reports a **prototype / pre-MVP, pre-revenue** company, approximately **$48K in founder funding**, no paying customers and no institutional capital. These are company disclosures carried forward for review, not independently audited accounts.

The revised deck labels pricing, account counts and validation thresholds as assumptions or proposed targets. It does not present future deployments, customer discussions, trials or performance goals as traction. Read the [evidence register](CLAIMS_AND_ASSUMPTIONS.md) alongside the deck.

## Rebuild the PDF

Use Python 3 with the dependencies listed in [requirements.txt](requirements.txt):

```sh
python -m pip install -r requirements.txt
python build_deck.py
```

The build writes `Triton_PreSeed_Deck_v4.pdf` in the repository root. It uses Arial when available on Windows, otherwise Helvetica, and preserves the navy/cyan identity and original observation-surface artwork. Text remains selectable in the PDF.

After editing, render and visually inspect all pages. Check text fit, source links, financial arithmetic and the distinction between evidence and assumptions before publishing.

## Repository layout

```text
index.html                       GitHub Pages PDF viewer
Triton_PreSeed_Deck_v4.pdf        Current network-first revision
build_deck.py                    Editable PDF generator
CLAIMS_AND_ASSUMPTIONS.md        Evidence and diligence companion
requirements.txt                Build dependencies
assets/observation-surfaces.png  Original deck artwork
```

Earlier PDFs remain available in the repository for version history. This repository contains the investor presentation and its source; it is not the operational Triton data platform.

---

**Triton Ocean Systems** · Jorge Pimentel, Founder & CTO

[Investor deck](https://triton-ocean-systems.github.io/investor-deck/index.html) · [GitHub repository](https://github.com/Triton-Ocean-Systems/investor-deck)
