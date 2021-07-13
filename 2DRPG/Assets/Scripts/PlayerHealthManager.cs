using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerHealthManager : MonoBehaviour
{
    private int player_current_health;
    public int player_max_health;


    void Start()
    {
        player_current_health = player_max_health;
    }

    // Update is called once per frame
    void Update()
    {

        if(player_current_health < 0)
        {
            FindObjectOfType<GameManager>().Endgame();
        }

    }

    public void HurtPlayer(int damage)
    {
        player_current_health -= damage;
    }
}
