---
layout: post
title:  "Equipment Grounding Options"
date:   2026-08-26 07:00:00 -0700
author: Mark Fussell
category: piece
filename: 2026-08-26-equipment-grounding-options

---

The following discusses the details and characteristics among different variations of equipment grounding and system earthing approaches when dealing with multiple power-producing subsystems.

It primarily focuses on how the behavior of ground faults across three subsystems
varies depending on the equipment-grounding approach between the subsystems.

 <!--more-->

#### [Table of Contents](#table-of-contents)

{% assign toc_path = "posts/" | append: page.filename | append: "_toc.txt" %}
{% include  {{toc_path}} %}

## [Overview ](#overview)

The following subsections show three simple subsystems (S1, S2, and S3) combined into an integrated macrosystem where the left subsystem (S1) has a battery power source/sink and the right subsystem (S3) has a solar power source.  The subsystem in between (S2) primarily sends power from S3 to S1, but the relationship to S1 is bidirectional (e.g. S2 has power from S1 when no solar power is present).  

The main details of the system will be documented in the first system variation (Three Independent Power Systems) to have a concrete example variation to work with.  But each section will describe the organization of the subsystems to each other and then the behavior of that system

## [SV-1: Three Independent Power Systems](#sv-1-three-independent-power-systems)

The following shows the situation if each power system is treated as completely independent for grounding and earthing considerations (all labeled as 'separately derived system' by NEC).  Given they are independent, they must manage their own Equipment Grounding Mesh [Equipment Grounding Mesh](/topics/#equipment-grounding-mesh) (EGM) and Earthing.  So they each have an SBJ ([System Bonding Jumper](/topics/#system-bonding-jumper)), their own [Earthing Electrode](/topics/#earthing-electrode) (EE or GE), and an appropriate mesh of connected [Equipment Grounding Conductors](/topics/#equipment-grounding-conductor) (EGCs). 

In this configuration, there is _no interconnection_ of the different EGMs: no EGCs connecting between the subsystems.  The only electrical connection are a DC+ and DC- between subsystems.


#### [SV-1: S1,S2,S3](#sv-1-s1s2s3)

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830b_c20_cv1b.png" width="640" alt="Equipment Grounding" %}

Note that both the Battery and the MPPT (Solar Charge Controller) have a DC- that is common to their two conductors (labeled 'a' and 'b' and a dotted jumper across the device).  This connection comes from either an internal jumper (e.g. inside the MPPT) or through a common external busbar (e.g. the battery connections).

#### [Example Wire Sizes for Power](#example-wire-sizes-for-power)

To discuss equipment grounding later, it will be useful to specify a realistic set of wire sizes and amperages.  For this explanation the system will be defined as the following:
   * 48V nominal voltage
   * 10kW inverter (200A @ ~50V)
   * 6kW of Solar Power (30A @ 200V or 120A @ ~50V) 

To handle the current for this system we would need the following wire capacities:
   * S1a = 200A — 2/0 AWG • 70mm²
   * S1b ⇔ S2a = 120A — 2 AWG • 35mm²
   * S2b ⇔ S3 = 30A — 8 AWG • 10mm² 
     * Where the 8AWG could be 10AWG if the distance is short enough

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830b_c20_cv2.png" width="640" alt="Equipment Grounding" %}

Note the colors on the diagram match the color system described in [Ordinary Colors: Multidimensional Relationship]({% post_url 2026-06-18-ordinary-colors %}#multidimensional-relationship)


#### [Example Wire Sizes for Equipment Grounding](#example-wire-sizes-for-equipment-grounding)

To support the grounding of each system (discussed below) we will need the [SBJs](/topics/#system-bonding-jumper) to be sized as follows:
   * SBJ-1 = 65A for the 200A S1a — 6 AWG • 65mm²
   * SBJ-2 = 65A for the 120A S2a — 6 AWG • 65mm²
   * SBJ-3 = 30A for the 40A S3 — 10 AWG • 6mm²

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830b_c20_cv3.png" width="640" alt="Equipment Grounding" %}

This is just an example, but gives a feel for the likely difference in wire capacity for the various subsystems and their interconnections, and will show the capacity issues with some of the inter-subsystem equipment grounding configurations.


### [SV-1 • Ground Fault Examples](#sv-1--ground-fault-examples)

This subsection will be common to all variations and walks through ground faults occurring between the various DC+ wires (S1a+ through S3+) and the subssystem chassis (or anywhere grounded within that chassis).  The lightning icon connects the positive wire to where it contacted the equipment grounding.  After that the orange arrows shows how DC+ reaches its corresponding DC- so the system can open the OCP (breaker or fuse) and eliminate the ground fault.

If the subsystems are all independent, the SBJ is always traversed in the subsystem where the ground fault occurs, and from there it is either handled locally or crosses between subsystems on the appropriate DC- conductor to get back to the energy source.

#### [SV-1 • GF-1](#sv-1--gf-1)

GF-1 is a fault between S1a+ and the S1 enclosure.  This is handled locally to S1 via SBJ-1.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv11-15_Page_1.png" width="640" alt="Ground Fault" %}

#### [SV-1 • GF-2](#sv-1--gf-2)

GF-2 is a fault between S1b+ and the S1 enclosure, where the source of power to S1b+ was the battery within S1.  This is handled locally to S1 via SBJ-1.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv11-15_Page_5.png" width="640" alt="Equipment Grounding" %}

#### [SV-1 • GF-3](#sv-1--gf-3)

GF-3 is a fault between S1b+ [from S2a+] and the S1 enclosure, where the source of power to S1b+ was the charge controller from S2.  This traverses SBJ-1 and crosses DC- (S1b- ⇔ S2a-) back to S2.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv11-15_Page_4.png" width="640" alt="Equipment Grounding" %}

#### [SV-1 • GF-4](#sv-1--gf-4)

GF-4 is a fault between S2a+ and the S2 enclosure, where the source of power to S2a+ was the charge controller in S2.  This is handled locally to S2 via SBJ-2. 

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv11-15_Page_3.png" width="640" alt="Equipment Grounding" %}

#### [SV-1 • GF-5](#sv-1--gf-5)

GF-5 is a fault between S2b+ [from S3+] and the S2 enclosure, where the source of power to S2b+ was the solar panels in S3.  This traverses SBJ-2 and crosses DC- (S2b- ⇔ S3-) back to S3.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv11-15_Page_2.png" width="640" alt="Equipment Grounding" %}

#### [SV-1 • GF-6](#sv-1--gf-6)

GF-6 is a fault between S3+ and the S3 enclosure, where the source of power to S3+ was the solar panels in S3.  This is handled locally to S3 via SBJ-3.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830b_c20_cv11-16_Page_2.png" width="640" alt="Equipment Grounding" %}

## [SV-2: Unified System Equipment Grounding Mesh](#sv-2-unified-system-equipment-grounding-mesh)

An alternative to SV-1 (Three Independent Power Systems) is to unify all three subsystems into a single [Equipment Grounding Mesh](/topics/#equipment-grounding-mesh) (EGM).  In that case there is only one [SBJ](/topics/#system-bonding-jumper), one [Earthing Electrode](/topics/#earthing-electrode) and one [EEC](/topics/#earthing-electrode-conductor) for the full system.  All [EGCs](/topics/#equipment-grounding-conductor) are interconnected into a single mesh with appropriate conductivity for the given coverage area.  

With this approach, the location of the SBJ and GEC/GE could be any one of the three 'boxes' and electrically (if not practically given other considerations) they would be identical as long as the conductivity was sufficient for all the EGC wires used when handling a given fault. 

### [SBJ and GEC Location Variations](#sbj-and-gec-location-variations)

The three variations for where the SBJ and GEC can be located are

#### [SV-2a: S1⇔S2⇔S3 • SBJ-1](#sv-2a-s1s2s3--sbj-1)

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv21-24_Page_4.png" width="640" alt="Equipment Grounding" %}


#### [SV-2b: S1⇔S2⇔S3 • SBJ-2](#sv-2b-s1s2s3--sbj-2)


{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv21-24_Page_3.png" width="640" alt="Equipment Grounding" %}


#### [SV-2c: S1⇔S2⇔S3 • SBJ-3](#sv-2c-s1s2s3--sbj-3)


{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv21-24_Page_2.png" width="640" alt="Equipment Grounding" %}

### [EGC Conductive Capacity](#egc-conductive-capacity)

Although all three variations above look identical in terms of electrical connectivity, they are not at all the same for the possible maximum current capacity and the safety of the system when we put in the number for our example system.

If we add the wire conductivity for the inter-subsystem EGCs they are likely to be:
   * EGC between S1 and S2 = 65A for the 120A S1b ⇔ S2a — 6 AWG • 65mm²
   * EGC between S2 and S3 = 30A for the 40A S2b ⇔ S3  — 10 AWG • 6mm²

This collection of wire capacities looks like the following:

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv21-24_Page_1.png" width="640" alt="Equipment Grounding" %}

It should already be apparent that some potential fault paths have too little capacity to successfully return the current back to the source.  But running through the Ground Faults from before, this should be even more visible.  

### [SV-2a • Ground Fault Examples](#sv-2a--ground-fault-examples)

Only the ground faults from above that behave differently in SV-2a vs. SV-1 are presented here.  SV-2a has the SBJ and GEC on S1, so all crossing of an SBJ must be routed to S1 via the inter-subsystem GECs.

#### [SV-2a • GF-4](#sv-2a--gf-4)

GF-4 is a fault between S2a+ and the S2 enclosure, where the source of power to S2a+ was the charge controller in S2.  This can no longer be handled locally to S2.  It must be routed over the S1 ⇔ S2 EGC, traverse SBJ-1, and cross DC- (S1b- ⇔ S2a-) back to S2

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv31.png" width="640" alt="Equipment Grounding" %}

#### [SV-2a • GF-5](#sv-2a--gf-5)

GF-5 is a fault between S2b+ [from S3+] and the S2 enclosure, where the source of power to S2b+ was the solar panels in S3.  It is routed over the S1 ⇔ S2 EGC, traverses SBJ-1, and crosses DC- (S1b- ⇔ S2a- ; S2b- ⇔ SS) back to S3

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv31-33_Page_2.png" width="640" alt="Equipment Grounding" %}

#### [SV-2a • GF-6](#sv-2a--gf-6)

GF-6 is a fault between S3+ and the S3 enclosure, where the source of power to S3+ was the solar panels in S3.  It is routed over the S3 ⇔ S2 EGC, then the S1 ⇔ S2 EGC, traverses SBJ-1, and crosses DC- (S1b- ⇔ S2a- ; S2b- ⇔ SS) back to S3

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv31-33_Page_1.png" width="640" alt="Equipment Grounding" %}


#### [EGC Capacities](#egc-capacities)

Although the above faults are somewhat circuitous, it can be seen that all the wires traversed are designed to handle at the current required to rapidly trigger the OCP.  In the worst case of GF-6 going through S2 and then S1, the EGC and DC- wiring is oversized compared to the needed conductivity and amperage.


{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv34.png" width="640" alt="Equipment Grounding" %}

## [SV-3: Paired Subsystems](#sv-3-paired-subsystems)

Instead of binding all three, we could just bind two of the systems together.  In the following System-2 (S2) and System-3 (S3) are bound together with two varations showing the choices for where the SBJ and GEC/GE could be located.

#### [SV-3a: S1,S2⇔S3 • SBJ-2](#sv-3a-s1s2s3--sbj-2)

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_15.png" width="640" alt="Equipment Grounding" %}

#### [SV-3b: S1,S2⇔S3 • SBJ-3](#sv-3b-s1s2s3--sbj-3)

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_16.png" width="640" alt="Equipment Grounding" %}

The same could be done with System-1 and System-2, with System-3 being the independent EG system.





### [SV-3a : S2 and S3 bound together • SBJ-2](#sv-3a--s2-and-s3-bound-together--sbj-2)

#### [SV-3a • GF-3](#sv-3a--gf-3)

Handled locally to S2.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_04.png" width="640" alt="Equipment Grounding" %}

#### [SV-3a • GF-4](#sv-3a--gf-4)

Traverses SBJ-2, and crosses DC- back to S3.  [Diagram is wrong]

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_05.png" width="640" alt="Equipment Grounding" %}

#### [SV-3a • GF-5](#sv-3a--gf-5)

Crosses EGC to S2, traverses SBJ-2, and crosses DC- back to S3.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_06.png" width="640" alt="Equipment Grounding" %}

### [SV-3b : S2 and S3 bound together • SBJ-3](#sv-3b--s2-and-s3-bound-together--sbj-3)


#### [SV-3b • GF-3](#sv-3b--gf-3)

Crosses EGC to S3, traverses SBJ-3, and crosses DC- back to S2.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_01.png" width="640" alt="Equipment Grounding" %}

#### [SV-3b • GF-4](#sv-3b--gf-4)

Crosses EGC to S3.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_02.png" width="640" alt="Equipment Grounding" %}

#### [SV-3b • GF-5](#sv-3b--gf-5)

Handled locally to S3.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_03.png" width="640" alt="Equipment Grounding" %}

## [Summary](#summary)

