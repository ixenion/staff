// just pause between 2 functions for exmpl

using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{
	public float waitSeconds;
	// use once
	void Start ()
	{
		StartCoroutine("coRoutineTest", 2f);// 2f passed as a coRoutine func. parameter
		// the same
		StartCoroutine(coRoutineTest(2f));// 2f passed as a coRoutine func. parameter
	}

	// update is called once per frame
	void Update ()
	{
		
	}

	IEnumerator coRoutineTest(waitTime){
		Debug.Log("Co Routine started");
		yield return new WaitForSeconds(waitTime);// waitTime seconds
		Debug.Log("Co routine ended");
}
