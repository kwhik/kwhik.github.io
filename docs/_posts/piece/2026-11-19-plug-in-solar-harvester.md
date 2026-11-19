---
layout: post
title:  "Plug-In Solar Harvester"
date:   2026-11-19 08:00:00 -0800
author: Mark Fussell
category: piece
filename: 2026-11-19-plug-in-solar-harvester

---

The "Plug-In Solar Harvester" (PISH) described here is a 48V system that has an MPPT putting energy into a 48V Battery along with supplying that energy to a 'micro-inverter' (MI) (at ~50V).   <!--more-->  While the sun is up, the energy to the MI is capped by the MI output to the AC-system but the rest of the energy is still harvested and goes into the battery.  When the sun goes down, the battery supplies the MI until it drains to a low-water-mark that risks the system turning off.  The next day the cycle continues and again maximally harvests the solar energy and provides it throughout the day based on the MI power cap.

#### [Specifics for this system](#specifics-for-this-system)

This specific PISH is designed:
  * For 1kW of solar (based on an MPPT that has a maximum output of 20A @ 48Vₙ)
  * To store 1.5kWh using a 30A @ 48Vₙ battery
  * Using one or two MIs that outputting either one or two legs of 120V power
  * Potentially coupled with one or two CT meters to limit the MI power output
  * Using a low-voltage "battery-protect" cutoff switch to disable MI output

And the specific products for the above:
  * A Victron 100V/20A MPPT
  * LiTime 30Ah 48V battery
  * AP Systems EZ1
  * AP Systems APmeter
  * A Victron 48V 100A Battery Protect 

It also has a T-Class (fast and high AIC) 300V fuse, a bunch of PV external wires and connectors, an optional shunt for better monitoring, etc.  It all fits into a large Packout case, and weighs almost 50lbs, mostly because of the battery.

#### [Pictures](#pictures)

The following pictures of the system are attached:
* The One-Microinverter version
* Top Shelf: Solar MPPT
* Bottom Shelf: Low-Voltage Cutoff
* The Two-Microinverter version
* House (Subpanel) Connection Overview
* CT Meters and Vue
* Junction Box (four out, two in)

##### [The One-Microinverter version](#the-one-microinverter-version)
{% include lightbox.html src="/images/posts/piece/2026-11-19-plug-in-solar-harvester/IMG_1423.png" width="640" alt="PISH: 1MI" %}

##### [Top Shelf: Solar MPPT](#top-shelf-solar-mppt)
{% include lightbox.html src="/images/posts/piece/2026-11-19-plug-in-solar-harvester/IMG_1435.png" width="640" alt="PISH: Top" %}

##### [Bottom Shelf: Low-Voltage Cutoff](#bottom-shelf-low-voltage-cutoff)
{% include lightbox.html src="/images/posts/piece/2026-11-19-plug-in-solar-harvester/IMG_1378.png" width="640" alt="PISH: Bottom" %}

##### [The Two-Microinverter version](#the-two-microinverter-version)
{% include lightbox.html src="/images/posts/piece/2026-11-19-plug-in-solar-harvester/IMG_1548.png" width="640" alt="PISH: 2MI" %}


##### [House (Subpanel) Connection Overview](#house-subpanel-connection-overview)
{% include lightbox.html src="/images/posts/piece/2026-11-19-plug-in-solar-harvester/IMG_1553.png" width="640" alt="CT Meters" %}

##### [CT Meters and Vue](#ct-meters-and-vue)
{% include lightbox.html src="/images/posts/piece/2026-11-19-plug-in-solar-harvester/IMG_1550.png" width="640" alt="CT Meters" %}

##### [Junction Box (four out, two in)](#junction-box-four-out-two-in)
{% include lightbox.html src="/images/posts/piece/2026-11-19-plug-in-solar-harvester/IMG_1552.png" width="640" alt="CT Meters" %}

## [Design Approach](#design-approach)

Plug-in solar takes a DC source of energy and supplies that energy onto an already running AC power system.  It is labeled 'Plug-in solar' because it assumes the energy is coming from solar panels, but… it doesn't necessarily have to.  Depending on the 'micro-inverter' (MI) [1], the DC energy source can be a battery (voltage-source) instead of a solar panel (current-source) and the micro-inverter will work fine.  Might not be 'warrantied' to work with a battery, but it is causing no harm to the product to use it that way [2].

The approach taken for this "Plug-In Solar Harvester" (PISH) system focuses on:
1. Harvesting as much energy as possible from the panels available
2. Providing that energy into an existing AC-system with minimal loss
3. Minimizing cost for the above

This approach is conceptually different from _powering_ through solar: there is no goal to provide all the power to any kind of load.  The power (energy per second) is irrelevant as long as the energy-per-day is maximally harvested and distributed.

The PISH described and shown above is designed to:
* Harvest about 4-5kWh a day through a 1kW solar source
* Provide about 3kWh (500W maximum for 6h) during daylight times
* Store the remaining 1+ kWh in the battery
* Provide the 1kWh for about two hours after sunset

A slightly upgraded PISH would use a 150V/45A MPPT, 2kW of solar, and 5kWh of storage to:
* Harvest about 8-10kWh a day
* Provide either 3kWh or 6kWh (500-1000W maximum for 6h) during daylight times
* Store the remaining 5kWh in the battery
* Provide the 5kWh for from five to ten hours after sunset

I also have a PISH variation with 20kWh of storage, which would enable "mostly offgrid" production of energy for some people, but it would still expect any transient power loads (say a microwave plus some power tools) to be provided by the grid itself and not the PISH.

## [Refs](#refs)

* [1] A micro-inverter is an AC-coupled inverter designed to function even if put _under_ a solar panel and exposed to the elements
* [2] Victron MPPTs have long been used as DC-DC voltage converters because they have certain features that DC-DC converters are missing.