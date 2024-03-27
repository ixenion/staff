// camera rotates by the target
using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{	
	public Transform target;
	// use once
	void Start ()
	{
		
	}

	// update is called once per frame
	void Update ()
	{
		transform.LookAt(target);
	}
}
