---
layout: page
title: Topics
permalink: /topics/
author: "Mark Fussell"
styles:
  - shiftRight1
---

<style>



/*================================== */
/*=== Topic-section in table styling */
/*================================== */






table tr:nth-child(1), /*A*/
table tr:nth-child(3), /*D*/
table tr:nth-child(4), /*E*/
table tr:nth-child(9), /*F*/
table tr:nth-child(10), /*G*/
table tr:nth-child(12), /*M*/
table tr:nth-child(13), /*S*/
table tr:nth-child(16), /*X*/

table tr:nth-child(1), /*Y*/
table tr:nth-child(1) /*Z*/
   {   
    color: #2e6da4;
    font-weight: bold;
    background-color: #deedf4;
  }

/*================================== */
/*=== Topic-Area Header Styling ===*/
/*================================== */



#ac,
#dc,
#earthing-electrode,
#floating-conductor,
#ground-fault,
#main-bonding-jumper,
#separately-derived-system,
#xiaflex,
#zzz
{
    color: #2e6da4;
    font-weight: bold;
    background-color: #deedf4;
    width: 100%;
    padding: 10px 10px; 
}

/*================================== */
/*================================== */
/*================================== */

</style>


The following entries contain information on topics, terms, acronyms, and abbreviations that are related to solar energy systems.

* *Index:*  &nbsp;&nbsp; [A-C](#a) &nbsp;•&nbsp; [D-F](#d) &nbsp;•&nbsp; [G-H](#g) &nbsp;•&nbsp; [I-L](#i) &nbsp;•&nbsp; [M-O](#m) &nbsp;•&nbsp; [P-S](#p) &nbsp;•&nbsp; [T-U](#t) &nbsp;•&nbsp; [V-Z](#v)
* *Entries:* &nbsp;&nbsp; [A&darr;](#ac) &nbsp;•&nbsp; [E&darr;](#earthing-electrode) &nbsp;•&nbsp; [G&darr;](#ground-fault) &nbsp;•&nbsp; [S&darr;](#short-circuit)

## Index

| Topic                                                                  | Alternate Name                          | 
|------------------------------------------------------------------------|-----------------------------------------|
|[AC &darr;](#ac) <a id="a"></a>|Alternating Current|
|[Arc &darr;](#arc)||
|[DC &darr;](#dc) <a id="d"></a>|Direct Current|
|[Earthing Electrode &darr;](#earthing-electrode) <a id="e"></a>|Grounding Electrode, EE, GE|
|[Earthing Electrode Conductor &darr;](#earthing-electrode-conductor)|Grounding Electrode Conductor, EEC, GEC|
|[Electrode &darr;](#electrode)||
|[Equipment Grounding Conductor &darr;](#equipment-grounding-conductor)|EGC|
|[Equipment Grounding Mesh &darr;](#equipment-grounding-mesh)|EGM|
|[Floating Conductor &darr;](#floating-conductor) <a id="f"></a>|Ungrounded Conductor, FC, UGC|
|[Ground Fault &darr;](#ground-fault) <a id="g"></a>||
|[Grounded Conductor &darr;](#grounded-conductor)|GC|
|[Main Bonding Jumper &darr;](#main-bonding-jumper) <a id="m"></a>|MBJ|
|[Separately Derived System &darr;](#separately-derived-system) <a id="s"></a>|SDS|
|[Short Circuit &darr;](#short-circuit)||
|[System Bonding Jumper &darr;](#system-bonding-jumper)|SBJ|

## Entries

{% comment %}
====================================================================================
====================================================================================
====================================================================================
{% endcomment %}


### [AC](#ac)

Alternating Current has a voltage curve that alternates from a positive value and a negative value, passing through zero twice in a full cycle.  For household electricity, AC is modeled after a mathematical sine wave and runs at from 50Hz to 60Hz.  

### [Arc](#arc)

An electric arc is a connection between two conductors through air.  It occurs when the conductance of the air is sufficient for current to flow between the voltage gap of the two conductors, at which point the arc itself increases the conductance of the air by ionizing it into a plasma.  To extinguish the arc (a) the voltage has to be lowered, (b) the conductors further separated to increase resistance, or (c) the air treated (cooled and deionized) to lower its conductance.

### [DC](#dc)

Direct Current supplies a voltage that is relatively stable over time.  It may increase or decrease based on system aspects (e.g. the charging of a battery or the changing of loads on the system) but these are variations around a desired static voltage.

### [Earthing Electrode](#earthing-electrode)

Called the Grounding Electrode (GE) in the NEC, the Earthing Electrode (EE) provide a relatively-low resistance connection to the physical earth and its voltage reference point.  The 'relatively-low' resistance is much higher than the high-conductance Equipment Grounding System: commonly as much as 25Ω.  But this resistance is much lower than the human body (less than one 40th) or other routes current could take when there is a voltage difference between the EGS and the earth.

### [Earthing Electrode Conductor](#earthing-electrode-conductor)

Called the Grounding Electrode Conductor (GEC) in the NEC, the Earthing Electrode Conductor (EEC) connects the Equipment Grounding System to the Earthing/Grounding Electrode (EE/GE)

### [Electrode](#electrode)

A conductor used to contact non-metal mediums like the dirt of the earth or the chemicals in a battery.

### [Equipment Grounding Conductor](#equipment-grounding-conductor)

An Equipment Grounding Conductor (EGC) provides a high-conductance electrical pathway between grounded parts of an Equipment Grounding System (EGS)

### [Equipment Grounding Mesh](#equipment-grounding-mesh)

The Equipment Grounding Mesh (EGM) is the interconnect network  of conductors providing a high-conductance ground reference frame for an electrical system.  Commonly bonded to the Earthing Electrode (EE or GE) via an Earthing Electrode Conducter (EEC or GEC)


### [Floating Conductor](#floating-conductor)

A Floating Conductor (FC) or Ungrounded Conductor (UGC) is a conductor that is not bonded to the Equipment Grounding System.  It if contacts any part of the EGS it is a Ground Fault.


### [Ground Fault](#ground-fault)

The contacting of a Floating Conductor and the Equipment Grounding System.



### [Grounded Conductor](#grounded-conductor)

A Grounded Conductor (GC) is a conductor that has been bonded to the Equipment Grounding System so its voltage is connected to the EGS and current can pass between the grounded conduct

### [Main Bonding Jumper](#main-bonding-jumper)

The Main Bonding Jumper (MPJ) is an SBJ (System Bonding Jumper) for the (assumed) primary grid power source.

### [Separately Derived System](#separately-derived-system)

A Separately Derived System (SDS) is the label given by the NEC to any power sources other than the (assumed) primary grid power source when the alternative power source manages its own EGM and Earthing.

### [Short Circuit](#short-circuit)

The direct contacting of two conductors that carry different voltages.

### [System Bonding Jumper](#system-bonding-jumper)

A System Bonding Jumper (SBJ) is a conductor that bonds the Equipment Grounding Mesh (EGM) to a grounded conductor (e.g. AC-Neutral or DC-).  In a Solar-powered system there are several power sources, and these can be organized as separate power systems (or Separately Derived System by NEC terms) that each need to manage their own grounding and earthing.

The Main Bonding Jumper (NEC term) is an SBJ for the main service entrance.

