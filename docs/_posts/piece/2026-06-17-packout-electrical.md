---
layout: post
title:  "Packout Portable Electrical System"
date:   2026-06-17 07:00:00 -0700
author: Mark Fussell
category: piece 
filename: 2026-06-17-packout-electrical
---

The following describes how to create a portable electrical system (storage, charging, and distribution) leveraging the Milwaukee® Packout™ storage system.  <!--more--> The main benefits of this approach are:
   * A very high level of portability (weight, transportability, weather resistance, etc.)
   * Flexibility in configuration
   * Good maximum power output (about 7.5kW)
   * Good storage (10 kWh).

The following two images provide the general concept and approach:

#### Wiring for a 200ah 12V cell
<img src="/images/posts/piece/2026-06-17-packout-electrical/IMG_9619_v2.png" width="360" alt="12V Cell Wiring" />

#### Connecting the system main DC stack and bus (for AC and Solar)

<img src="/images/posts/piece/2026-06-17-packout-electrical/IMG_9606_v2.png" width="360" alt="Main Stack" />

#### More Photos

##### DC Power

<img src="/images/posts/piece/2026-06-17-packout-electrical/IMG_9407.png" width="360" alt="XX" />

<img src="/images/posts/piece/2026-06-17-packout-electrical/IMG_9619_v2.png" width="360" alt="12V Cell Wiring" />

<img src="/images/posts/piece/2026-06-17-packout-electrical/IMG_9491.png" width="360" alt="XX" />

<img src="/images/posts/piece/2026-06-17-packout-electrical/IMG_9492.png" width="360" alt="XX" />

##### AC Power
<img src="/images/posts/piece/2026-06-17-packout-electrical/IMG_9617.png" width="360" alt="XX" />

<img src="/images/posts/piece/2026-06-17-packout-electrical/IMG_9604.png" width="360" alt="XX" />

##### Solar Power

<img src="/images/posts/piece/2026-06-17-packout-electrical/IMG_9605.png" width="360" alt="XX" />

<img src="/images/posts/piece/2026-06-17-packout-electrical/IMG_9606_v2.png" width="360" alt="Main Stack" />

<img src="/images/posts/piece/2026-06-17-packout-electrical/IMG_9538.png" width="360" alt="XX" />

##### BMS

<img src="/images/posts/piece/2026-06-17-packout-electrical/IMG_9634.png" width="360" alt="XX" />

#### Table of Contents

{% assign toc_path = "posts/" | append: page.filename | append: "_toc.txt" %}
{% include  {{toc_path}} %}

### [Introduction](#introduction)

There are a number of tradeoffs in the different approaches to building an electrical system (defined as a system that has electrical storage, charging, and distribution).  
* An all-in-one portable generator provides many desirable features in a relatively small form factor.  
* A larger 'installed' system can have higher capacities for both power and storage.  
* A 'dolly' combines some of the higher capacities into a somewhat moveable chassis.  
 
With each of the benefits of the approaches just mentioned, there are potentially corresponding penalties to price, flexibility, portability, and so on.

#### Portability

One major consideration to enabling a system to be portable is that the weight of the components can not be beyond the abilities of the user to move them.  For a generally useful electrical system the heaviest item is almost always going to be the battery, which weighs about 16-20 lbs (7-9kg) per kWh.  Managing this weight will be one of core aspects to the modular approach.  An additional requirement further defining portability is that it has to be possible to move the components without leveraging wheels and ramps.  Components must be carryable within normal human comfort levels: less than 50lbs.

Beyond the portability considerations, the other aspects are: 

* It should be possible to compose different variations for functional or financial goals; 
* It should be possible to create a system with >5kW of power generation, and
* It should be possible to have more than 5kWh of storage

#### Additional Aspects

To meet the above goals, additional approach aspects were added to help focus the potential solutions.  These include 

* Leveraging the functionality and sizes of the Packout™ tool boxes and organizers
* Utilizing modern wireless control systems
* Using reasonably-sized wires (otherwise the wires themselves become a burden).  This was ultimately constrained in the approach described to using wires no bigger than 35mm² (2 AWG), allowing a bit over 100A-sustained comfortably.  [[1]](#1) 
* Having a clean connector system so the system can be assembled and disassembled as rapidly as possible [[2]](#2)


### [Approach](#approach)

A core approach described herein is to leverage an unusually good match between the dimensions of the Packout™ Compact Tool Box and the size of the 206Ah LiFePO4 prismatic cell.  Four 206Ah cells easily fit in width, height, and depth within the compact toolbox.  This produces a 12V nominal battery with room for a BMS on top and connectors in the forward section.

A second core approach is to use the sides of the Packout™ system as the connector location and 'bus' of the system.  The main power bus can be on either side but in this version it is shown  to be on the right side when facing a system stack.  Since a Compact Tool Box is only half-width, there is also an internal portal between the left and right Tool Box that allows combining two boxes without external connection.  Full-width boxes have access to both the left and the right side for either bus or additional port connections.

By using the sides instead of the front, back, or top, the system is easier to work with individually (multiple portal locations are available on the sides without impeding the toolbox functionality of hinges and stacking) and in standard Packout™ stacks of three or more layers (potentially on a dolly) where the sides are commonly accessible when the back (for example) would likely be inaccessible.  At worse, a bit of breathing space needs to be maintained between stacks to allow for the 'bus' portals and wiring.

### [Walkthrough "Demo"](#walkthrough-demo)

The following walks through a completed system to provide context for the subsequent description.

#### Battery Cells

The four 206Ah prismatic cells (e.g. LF206: <https://www.evlithium.com/LiFePO4-Battery/eve-prismatic-cells-206ah.html>) can fit into the compact toolbox with room to spare on the sides, front, and top.  To keep these cells in position and compressed to avoid expansion, they are sandwiched between two end plates.



#### BMS

Although the original cells were sources by deconstructing a SOK battery, I upgraded the BMS to a JK for better control, visibility, and power.  Especially being able to turn off the BMS enables avoiding having a physical switch or constantly hot wires.



#### Primary Power Bus

The main power bus is run between 3/8 (M10) bulkhead pass-through terminals that support about 200A (2/0 or 70mm² equivalent).  The wires are 2AWG (35mm²) so the system is targeting a bit under 150A maximum continuous load, but should be able to handle transitory spikes above that without significant heating.  Fuses are at 150A although possibly should be a bit higher if they are relatively fast acting.

The primary power bus is at whatever voltage is desired.  Each 'cell' produces 12V but two can be combined horizontally and a total of four can be easily combine vertically.  

#### Secondary Power Bus

A secondary power bus is run at lower amperage through either Anderson PP15 or 20A Cigarette Lighter ports.  The cigarette lighter port has the advantage of structural strength, easy accessory support, and is cheaper.  The main advantage of using PP15 is that two 2-pole ports can be combined in the same space.

#### Internal Portal


### [Description](#description)


### [Summary](#summary)


## [Footnotes](#footnotes)

* [1] <a id="1"/> Conceptually it would be possible to get all the way to 200A, but the wires would have to be significantly heavier and some space constraints would be hard to meet.
* [2] <a id="2"/> The connectors add an expense that can be avoided in exchange for longer setup and teardown times but without any loss of functionality otherwise..
