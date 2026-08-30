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

## [Overview](#overview)

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
   * 48V nominal system voltage
   * 10kW inverter (200A @ ~50V) connected to S1a 
   * 6kW of Solar Power (30A @ 200V or 120A @ ~50V) provided by S3

To handle the current requirement for this system we would need the following wire capacities:
   * S1a = 200A — 2/0 AWG • 70mm²
   * S1b ⇔ S2a = 120A — 2 AWG • 35mm²
   * S2b ⇔ S3 = 30A — 8 AWG • 10mm² 
     * Where this could alternatively be 10AWG • 6mm² if the distance is short enough

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830b_c20_cv2.png" width="640" alt="Equipment Grounding" %}

Note the colors for the wire capacities on the diagram match the color system described in [Ordinary Colors: Multidimensional Relationship]({% post_url 2026-06-18-ordinary-colors %}#multidimensional-relationship)


#### [Example Wire Sizes for Equipment Grounding](#example-wire-sizes-for-equipment-grounding)

To support the grounding of each system (discussed below) we will need the [SBJs](/topics/#system-bonding-jumper) to be sized as follows:
   * SBJ-1 = 65A for the 200A S1a — 6 AWG • 65mm²
   * SBJ-2 = 65A for the 120A S2a — 6 AWG • 65mm²
   * SBJ-3 = 30A for the 40A S3 — 10 AWG • 6mm²

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830b_c20_cv3.png" width="640" alt="Equipment Grounding" %}

This is just an example system, but gives a proper feel for the likely difference in wire capacity for the various subsystems and their interconnections, and it will show the capacity issues with some of the inter-subsystem equipment grounding configurations.


### [SV-1 • Ground Fault Examples](#sv-1--ground-fault-examples)

This 'Ground Fault Examples' section is common to all system variations and walks through ground faults occurring between the various DC+ wires (S1a+ through S3+) and the subssystem chassis (or anywhere grounded within that chassis).  The lightning icon connects the positive wire to where it contacted the equipment grounding.  After that the orange arrows shows how DC+ reaches its corresponding DC- so the system can open the OCP (breaker or fuse) and eliminate the ground fault.

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

### [SV-2 • SBJ and GEC Location Variations](#sv-2--sbj-and-gec-location-variations)

The three variations for where the SBJ and GEC can be located are as follows.

#### [SV-2a: S1⇔S2⇔S3 • SBJ-1](#sv-2a-s1s2s3--sbj-1)

Placed on S1 (as SBJ-1)

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv21-24_Page_4.png" width="640" alt="Equipment Grounding" %}


#### [SV-2b: S1⇔S2⇔S3 • SBJ-2](#sv-2b-s1s2s3--sbj-2)

Placed on S2 (as SBJ-2)

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv21-24_Page_3.png" width="640" alt="Equipment Grounding" %}


#### [SV-2c: S1⇔S2⇔S3 • SBJ-3](#sv-2c-s1s2s3--sbj-3)

Placed on S3 (as SBJ-3)

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv21-24_Page_2.png" width="640" alt="Equipment Grounding" %}

### [SV-2 • EGC Capacities](#sv-2--egc-capacities)

Although all three variations above look identical in terms of electrical connectivity, when we put in the conductor capacity numbers for our example system they become clearly dissimilar.  And they do not equivalently (and for-some properly) handle ground faults throughout the system.  

If we add the wire conductivity for the inter-subsystem EGCs they should be:
   * EGC between S1 and S2 = 65A for the 120A S1b ⇔ S2a — 6 AWG • 65mm²
   * EGC between S2 and S3 = 30A for the 40A S2b ⇔ S3  — 10 AWG • 6mm²

This collection of wire capacities looks like the following:

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv21-24_Page_1.png" width="640" alt="Equipment Grounding" %}

It should already be apparent that some potential fault paths have too little capacity to successfully return the current back to the source.  But running through the Ground Faults from before, this should be even more visible.  

### [SV-2a • Ground Fault Examples](#sv-2a--ground-fault-examples)

Only the ground faults from above that behave differently in SV-2a vs. SV-1 are presented here.  SV-2a has the SBJ and GEC on S1, so all crossing of an SBJ must be routed to S1 via the inter-subsystem EGCs.

#### [SV-2a • GF-4](#sv-2a--gf-4)

GF-4 is a fault between S2a+ and the S2 enclosure, where the source of power to S2a+ was the charge controller in S2.  This can no longer be handled locally to S2.  It must be routed over the S1 ⇔ S2 EGC, traverse SBJ-1, and cross DC- (S1b- ⇔ S2a-) back to S2

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv31.png" width="640" alt="Equipment Grounding" %}

#### [SV-2a • GF-5](#sv-2a--gf-5)

GF-5 is a fault between S2b+ [from S3+] and the S2 enclosure, where the source of power to S2b+ was the solar panels in S3.  It is routed over the S1 ⇔ S2 EGC, traverses SBJ-1, and crosses DC- (S1b- ⇔ S2a- ; S2b- ⇔ S3) back to S3

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv31-33_Page_2.png" width="640" alt="Equipment Grounding" %}

#### [SV-2a • GF-6](#sv-2a--gf-6)

GF-6 is a fault between S3+ and the S3 enclosure, where the source of power to S3+ was the solar panels in S3.  It is routed over the S3 ⇔ S2 EGC, then the S1 ⇔ S2 EGC, traverses SBJ-1, and crosses DC- (S1b- ⇔ S2a- ; S2b- ⇔ S3) back to S3

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv31-33_Page_1.png" width="640" alt="Equipment Grounding" %}


#### [SV-2a • EGC Capacities](#sv-2a--egc-capacities)

Although the above faults are somewhat circuitous, it can be seen that all the wires traversed are designed to handle at the current required to rapidly trigger the OCP.  In the worst case of GF-6 going through S2 and then S1, the EGC and DC- wiring is oversized compared to the needed conductivity and amperage.


{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv34.png" width="640" alt="Equipment Grounding" %}

### [SV-2c • Ground Fault Examples](#sv-2c--ground-fault-examples)

Switching to the complete opposite side subsystem for the SBJ and GEC: SV-2c has the SBJ and GEC on S3, so all crossing of an SBJ must be routed to S3 via the inter-subsystem EGCs.  We actually only need to look at one ground fault to see the core problem with this variation.

#### [SV-2c • GF-1](#sv-2c--gf-1)

GF-1 is a fault between S1a+ and the S1 enclosure, where the source of power to S1a+ was the battery in S1.  The current for this fault is routed over the S1 ⇔ S2 EGC, then the S2 ⇔ S3 EGC, then  traverses SBJ-3, and crosses DC- (S3- ⇔ S2b; S2a- ⇔ S1b-) back to S1 and the battery.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv41-42_Page_1.png" width="640" alt="Equipment Grounding" %}

#### [SV-2c • EGC Capacities](#sv-2c--egc-capacities)

The GF-1 fault is again quite circuitous but this time it is handling a 200A fault with as small as a 30A-rated conductor (the S2 ⇔ S3 EGC). 

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv41-42_Page_2.png" width="640" alt="Equipment Grounding" %}

Clearly we can not have the case where a subsystem dealing with significantly smaller currents (and with an [EGM](/topics/#equipment-grounding-mesh) designed for these smaller currents) is expected to handle the faults of higher-current subsystems.  S1 and S2 have the same EGC requirements (AWG 6) for the example system, so the SBJ/GEC could be on either of these two systems.  S1 would be preferable because it is the one most driving the EGC requirement and a 'little' increase (e.g. to 300A+ wiring) would cause it to need to upgrade its SBJ and other EGM aspects.

Under no circumstances can S3 be made to handle the equipment grounding requirements of S1 or S2.

## [SV-3: Paired Subsystems](#sv-3-paired-subsystems)

Instead of having SV-1 (Three Independent Power Systems) or SV-2 (A Unified System Equipment Grounding Mesh), we could split the three systems into two pieces.  Given the issues described above with the EGC capacity, and the similarity in grounding between S1 and S2 (along with the bidirectional power-flow aspect between the two systems), the only reasonable variation seems to be:
   * Pair S1 & S2 into a single EGM
   * Have S3 have its own EGM independent of S1 & S2

This system architectural variation will be called SV-3.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830c_c20_cv51-53_Page_1.png" width="640" alt="Equipment Grounding" %}

### [SV-3 • Ground Fault Examples](#sv-3--ground-fault-examples)

There are no new ground-fault paths for SV-3: the paths that a fault takes will either be from SV-1 or from SV-2a.  Showing the example of that for GF-5 below, the path is identical where the unused EGC from S2 to S3 is simply not present.


#### [SV-3 • GF-5](#sv-3--gf-5)

GF-5 is a fault between S2b+ [from S3+] and the S2 enclosure, where the source of power to S2b+ was the solar panels in S3.  It is routed over the S1 ⇔ S2 EGC, traverses SBJ-1, and crosses DC- (S1b- ⇔ S2a- ; S2b- ⇔ S3) back to S3

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830d_c20_cv52-53_Page_2.png" width="640" alt="Equipment Grounding" %}

### [SV-3 • EGC Capacities](#sv-3--egc-capacities)

As was true in SV-2a, the EGC capacity for the circuitous flow of GF-5 uses wires with larger capacity than the S3+ ground-fault requires.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260830d_c20_cv52-53_Page_1.png" width="640" alt="Equipment Grounding" %}

### [SV-3 Discussion](#sv-3-discussion)

The SV-3 variation has one significant advantage of SV-2a: it handles ground faults (e.g. GF-6) properly when the S3 system is not connected to S2.  This advantage is quite signficant if S3 is:

* At times intentionally disconnected from S2 such that the S2- ⇔ S3- conductor is not available as a return path
* Attached to alternate collectors and harvesters, which would require rewiring the EGC along with the S3+/S3- power conductors.
* Very far away from S2, where a continuity disruption could occur along the S2 ⇔ S3 path
* Attached to other conductors and environments than S2, increasing the importance of reacting to S3 ground faults without possible (somewhat obscure or even invisible) failures.


## [Summary](#summary)

