---
layout: post
title:  "Equipment Grounding Options"
date:   2026-08-26 07:00:00 -0700
author: Mark Fussell
category: piece
filename: 2026-08-26-equipment-grounding-options

---

The following discusses the details and characteristics among different variations of equipment grounding and system earthing approaches when dealing with multiple power-producing subsystems.

It primarily focuses on how the behavior of ground faults across a three-system macrosystem varies depending on the equipment-grounding approach.

 <!--more-->

#### [Table of Contents](#table-of-contents)

{% assign toc_path = "posts/" | append: page.filename | append: "_toc.txt" %}
{% include  {{toc_path}} %}

## [Overview ](#overview)

The following subsections show a simple three-system (S1, S2, and S3) combined into an integrated macrosystem where the left system (S1) has a battery power source/sink and the right system (S3) has a solar power source.  The system in between (S2) primarily sends power from S3 to S1 although the relationship to S1 is bidirectional (e.g. S2 has power from S1 when no solar power is present).  

The Battery and the MPPT (Solar Charge Controller) both have common a neutral that is  on both the left and right.  This is achieved either internally (e.g. for the MPPT) or externally (e.g. through a busbar).  

### [SV-1: Independent Systems](#sv-1-independent-systems)

The following shows the situation if each system is treated as completely independent for grounding and earthing considerations.  They each have their own SBJ (System Bonding Jumper) and their own GE (Grounding Electrode / Earthing Electrode) and GEC (Grounding Electrode Conductor)


#### [SV-1: S1,S2,S3](#sv-1-s1s2s3)

{% include lightbox.html src="/images/posts/piece/2026-08-26-equipment-grounding-options/Kwhik_PergVault_mlf260825a_c20_cv1-33_Page_17.png" width="640" alt="Equipment Grounding" %}


### [SV-2: Single EG System and GE](#sv-2-single-eg-system-and-ge)

On the other extreme, all three systems can be tied together into one EG (Equipment Grounding) system, one SBJ for that system, and one GEC/GE for that system.  The location of the SBJ and GEC/GE could be any one of the three 'boxes'. 

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
