<br>

# Background and Project Understanding

<br>

***Source Datafile Links***

[Multivariate Gait Data](https://archive.ics.uci.edu/dataset/760/multivariate+gait+data)
[Associated Paper](https://www.semanticscholar.org/paper/Smoothing-spline-analysis-of-variance-models%3A-A-new-Helwig-Shorter/67cf199e6fe5619c24213abe53341e48f82a0012)


---

<br><br>

***Definition of Gait***

---
> Gait is the particular manner, style, or pattern in which a person or animal walks or runs.

> Another definition is:  Gait consist of a person's or animal's specific manner, style, or pattern of walking, running, or moving on foot.

<br>
<ins>Key Definitions</ins>

* Human Walking: The coordinated movement of feet, legs, hips, and arms influenced by balance, muscle strength, and speed.
* Animal Movement: A specific sequence of footfalls used by animals like horses or dogs (such as a walk, trot, canter, or gallop).
* Rate of Progress: A metaphorical or literal steady rhythm of movement (e.g., "a leisurely gait").
* Pronunciation: Pronounced /ɡeɪt/ (rhymes with "mate", not "gate").

<br><br>

<ins>Key Aspects of Gait</ins>

Walking Pattern: It describes how your feet strike the ground, how weight shifts from one leg to the other, and how your joints, muscles, and nerves coordinate movement.

Gait Cycle: A single walking cycle is split into two main parts according to the Cleveland Clinic Guide to Gait Disorders:

* Stance Phase (about 60%): When your foot is touching and supporting your weight on the ground (from heel strike to toe-off).
* Swing Phase (about 40%): When your foot is lifted and moving forward through the air.
	
_Abnormal Gait: An altered or unusual walking pattern (such as limping, shuffling, or waddling) often points to underlying pain, joint arthritis, muscle weakness, or a neurological condition._

<br><br>

<ins>Common Types of Gait</ins>

* Normal Gait: A smooth, balanced, and rhythmic walking cycle split into stance (about 60%) and swing (about 40%) phases.
* Antalgic Gait: A limping pattern adopted to minimize pain in a leg, foot, or joint.
* Parkinsonian / Propulsive Gait: Short, shuffling steps with a reduced arm swing, often seen in Parkinson's disease.
* Ataxic Gait: An uncoordinated, wide-based, unsteady walk.

https://www.hingehealth.com/resources/glossary/gait/

<br><br>


---
***Gait Cycles vs Steps***

---
Consecutive gait cycles are not the same as steps.

One gait cycle, or stride, is defined as two consecutive heel strikes of the same limb. Each gait cycle is composed of two steps.

	* Gait Cycle: The complete movement sequence from the time one foot makes contact with the ground until that same foot makes contact with the ground again (equal to one full stride).
	* Step: Half of a gait cycle, measured from the initial contact of one foot to the initial contact of the opposite foot.

	*Key Differences*

		* Duration/Coverage: One complete gait cycle contains two steps (one left step and one right step).
		* Reference Foot: A gait cycle tracks a single limb from start to finish (e.g., right heel strike to right heel strike), whereas a step alternates between two different limbs (e.g., left heel strike to right heel strike).

<br><br>


---
***Gait changes and Understanding The Cycles***

This numbering system represents the normalized timeline of a single stride, tracking a leg's movement from the exact moment one heel hits the ground until that same heel hits the ground again.
Instead of measuring walking in seconds, researchers and clinicians use a 0% to 100% scale to compare data easily, regardless of how fast or slow a person is moving.

<ins>Key Milestones in the 0–100% Cycle</ins>

The cycle is broken down into specific events for the tracked leg:

* 0% (Initial Contact): The heel strikes the ground. This marks the absolute beginning of the cycle and the start of the Stance Phase.
* 0% to 10% (Loading Response): The foot flattens, and the leg absorbs the impact of body weight.
* 10% to 30% (Mid-Stance): The body weight shifts entirely over the stationary foot while the opposite foot is in the air.
* 30% to 50% (Terminal Stance): The heel lifts off the ground, and the body moves forward past the foot.
* 50% to 60% (Pre-Swing / Toe-Off): The big toe pushes off the ground at roughly 60%. This ends the Stance Phase and transitions the leg into the air.
* 60% to 100% (Swing Phase): The foot leaves the ground, swings forward through the air, and prepares for the next step.
* 100% (Next Initial Contact): The same heel strikes the ground again, completing the cycle and instantly starting the next one at 0%.


---


<br><br>

<br>
<br>
<br>

