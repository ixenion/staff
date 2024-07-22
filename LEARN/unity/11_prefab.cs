// prefab - reusable object
using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{
	public GameObject ball;
	// use once
	void Start ()
	{
		Instantiate(ball, transform.position, transform.rotation);
		// to repeatedly call anoter function:
		InvokeRepeating("inst", 1f, 1f);// method, delay, repeat number
	}

	// update is called once per frame
	void Update ()
	{

	}

	void inst(){
		Instantiate(ball, transform.position, transform.rotation);
	}
}
