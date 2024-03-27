using UnityEngine;
using System.Colletions;

public class TestScript : MonoBehaviour
{
	// use once
	void Start ()
	{
		// available at inspector and in other scripts
		public int a;
		// not available in inspector and not av. in other scripts
		private int b;
		// available at inspector but not av. in other scripts
		[SerializeField]
		private int c;
		
		// not av at inspector but av in other scripts
		[HideInInspector]
		public int d;
	}

	// update is called once per frame
	void Update ()
	{

	}
}
