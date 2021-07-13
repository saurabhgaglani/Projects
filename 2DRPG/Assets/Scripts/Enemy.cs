using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy : MonoBehaviour
{

    public float speed;
    public float stoppingDistance;

    private float timebtShots;
    public float startTimebtShots;

    public GameObject projectile;

    private Transform player;
    private Transform enemy;

    void Start()
    {
        player = GameObject.FindGameObjectWithTag("Player").transform;
        timebtShots = startTimebtShots;
    }


    void Update()
    {
        if (Vector2.Distance(transform.position, player.position) > stoppingDistance)
        {
            transform.position = Vector2.MoveTowards(transform.position, player.position, speed * Time.deltaTime);
        }

        else
        {
            transform.position = this.transform.position;
        }


        if (timebtShots <= 0)
        {
            Instantiate(projectile, transform.position, Quaternion.identity);
            timebtShots = startTimebtShots;
        }

        else
        {
            timebtShots -= Time.deltaTime;
        }
    }



    void OnTriggerEnter2D(Collider2D other)
    {

        if (other.CompareTag("Enemy"))
        {
            GameObject ghit = other.gameObject;
            Transform thit = ghit.transform;

            transform.position = new Vector2(thit.position.x + 2, thit.position.y + 2);
        }
    }
}