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

Note that both the Battery and the MPPT (Solar Charge Controller) have a DC- that is common to their two conductors (left and right from their 'boxes').  This connection comes from either an internal jumper (e.g. inside the MPPT) or through a common external busbar (e.g. the battery connections).  

### [SV-1: Three Independent Power Systems](#sv-1-three-independent-power-systems)

The following shows the situation if each power system is treated as completely independent for grounding and earthing considerations (all labeled as 'separately derived system' by NEC).  Given they are independent, they must manage their own Equipment Grounding Mesh [Equipment Grounding Mesh](/topics/#equipment-grounding-mesh) (EGM) and Earthing.  So they each have an SBJ ([System Bonding Jumper](/topics/#system-bonding-jumper)), their own [Earthing Electrode](/topics/#earthing-electrode) (EE or GE), and an appropriate mesh of connected [Equipment Grounding Conductors](/topics/#equipment-grounding-conductor) (EGCs). 

In this configuration, there is _no interconnection_ of the different EGMs: no EGCs connecting between the systems.  The only electrical connection are a DC+ and DC- between systems.


#### [SV-1: S1,S2,S3](#sv-1-s1s2s3)

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_17.png" width="640" alt="Equipment Grounding" %}


### [SV-2: Single EG System and GE](#sv-2-single-eg-system-and-ge)

On the other extreme, all three subsystems can be tied together into one [Equipment Grounding Mesh](/topics/#equipment-grounding-mesh) (EGM).  In that case there is only one [SBJ](/topics/#system-bonding-jumper), one [Earthing Electrode](/topics/#earthing-electrode) and one [EEC](/topics/#earthing-electrode-conductor) for the full system.  All [EGCs](/topics/#equipment-grounding-conductor) are interconnected into a single mesh with appropriate conductivity for the given coverage area.  

With this approach, the location of the SBJ and GEC/GE could be any one of the three 'boxes' and electrically (if not practically given other considerations) they would be identical as long as the conductivity of the EGC wires was sufficient.

#### [SV-2a: S1⇔S2⇔S3 • SBJ-1](#sv-2a-s1s2s3--sbj-1)

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_12.png" width="640" alt="Equipment Grounding" %}

#### [SV-2b: S1⇔S2⇔S3 • SBJ-2](#sv-2b-s1s2s3--sbj-2)

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_13.png" width="640" alt="Equipment Grounding" %}

#### [SV-2c: S1⇔S2⇔S3 • SBJ-3](#sv-2c-s1s2s3--sbj-3)

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_14.png" width="640" alt="Equipment Grounding" %}

### [SV-3: Binding System-2 and System-3 into one EG System](#sv-3-binding-system-2-and-system-3-into-one-eg-system)

Instead of binding all three, we could just bind two of the systems together.  In the following System-2 (S2) and System-3 (S3) are bound together with two varations showing the choices for where the SBJ and GEC/GE could be located.

#### [SV-3a: S1,S2⇔S3 • SBJ-2](#sv-3a-s1s2s3--sbj-2)

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_15.png" width="640" alt="Equipment Grounding" %}

#### [SV-3b: S1,S2⇔S3 • SBJ-3](#sv-3b-s1s2s3--sbj-3)

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_16.png" width="640" alt="Equipment Grounding" %}

The same could be done with System-1 and System-2, with System-3 being the independent EG system.


## [Ground Fault Examples](#ground-fault-examples)

The following subsections walk through ground faults occurring in the various systems (S1, S2, and S3) and from the different energy sources.  The lightning icon connects the positive wire to where it contacted the equipment grounding.  After that the orange arrows shows how DC+ reached DC- [if possible]

### [Variation-1 : All Independent Systems](#variation-1--all-independent-systems)

If the systems are all independent, the SBJ is always traversed in the system where the ground fault occurs, and from there it is either handled locally or crosses between systems on the DC- conductor.

#### [SV-1 • GF-1](#sv-1--gf-1)

Handled locally to S1.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_07.png" width="640" alt="Equipment Grounding" %}

#### [SV-1 • GF-2](#sv-1--gf-2)

Traverses SBJ-1, and crosses DC- back to S2.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_08.png" width="640" alt="Equipment Grounding" %}

#### [SV-1 • GF-3](#sv-1--gf-3)

Handled locally to S2.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_09.png" width="640" alt="Equipment Grounding" %}

#### [SV-1 • GF-4](#sv-1--gf-4)

Traverses SBJ-2, and crosses DC- back to S3.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_10.png" width="640" alt="Equipment Grounding" %}

#### [SV-1 • GF-5](#sv-1--gf-5)

Handled locally to S3.

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_11.png" width="640" alt="Equipment Grounding" %}



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
