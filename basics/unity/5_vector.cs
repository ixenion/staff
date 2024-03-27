using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{
	Vector2// stores 2 value inside
	Vector3
	Vector4

	Vector2 pos;
	// use once
	void Start ()
	{
		pos = new Vector2 (5f, 6f);
		Debug.Log(pos.x);// prints x coor
		Debug.Log(pos.y);
	}

	// update is called once per frame
	void Update ()
	{

	}
}
