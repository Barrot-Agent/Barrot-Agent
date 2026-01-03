
## CHAMBER_CREATED
**Timestamp:** 2026-01-03T21:23:20.272299+00:00

```json
{
  "chamber_id": "test_chamber_1",
  "mode": "forecast"
}
```

## SIMULATION_COMPLETED
**Timestamp:** 2026-01-03T21:23:20.272475+00:00

```json
{
  "chamber_id": "test_chamber_1",
  "scenario": {
    "directives": [
      {
        "name": "TEST_DIRECTIVE"
      }
    ]
  },
  "started_at": "2026-01-03T21:23:20.272443+00:00",
  "outcomes": [
    {
      "directive": {
        "name": "TEST_DIRECTIVE"
      },
      "predicted_impact": {
        "memory_impact": "low",
        "matrix_impact": "medium",
        "council_impact": "high"
      },
      "confidence": 0.75
    }
  ],
  "completed_at": "2026-01-03T21:23:20.272450+00:00"
}
```

## CHAMBER_CLOSED
**Timestamp:** 2026-01-03T21:23:20.272579+00:00

```json
{
  "chamber_id": "test_chamber_1",
  "results": {
    "chamber_id": "test_chamber_1",
    "mode": "forecast",
    "active": false,
    "state": {
      "created": "2026-01-03T21:23:20.272242+00:00",
      "agents": [
        {
          "id": "agent_0",
          "name": "Test Agent",
          "config": {
            "name": "Test Agent",
            "type": "forecaster"
          },
          "mutations": [],
          "added_at": "2026-01-03T21:23:20.272433+00:00"
        }
      ],
      "directives": [
        {
          "directive": {
            "name": "TEST_DIRECTIVE"
          },
          "injected_at": "2026-01-03T21:23:20.272440+00:00",
          "impact": null
        },
        {
          "directive": {
            "name": "TEST_DIRECTIVE"
          },
          "injected_at": "2026-01-03T21:23:20.272447+00:00",
          "impact": null
        }
      ],
      "glyphs_emitted": [],
      "council_votes": [],
      "reality_drift": 0.0,
      "closed_at": "2026-01-03T21:23:20.272555+00:00"
    }
  }
}
```

## DIRECTIVE_FORECAST_GLYPH
**Timestamp:** 2026-01-03T21:23:20.273055+00:00

```json
{
  "forecast": {
    "directive_name": "MEMORY_ENHANCEMENT_DIRECTIVE",
    "forecast_time": "2026-01-03T21:23:20.272993+00:00",
    "impacts": {
      "memory": "high",
      "matrix": "low",
      "council": "low"
    },
    "confidence": 0.85,
    "risks": [
      {
        "area": "memory",
        "risk": "High impact on memory may cause instability",
        "severity": "high"
      }
    ],
    "opportunities": [
      {
        "area": "memory",
        "opportunity": "Potential for memory enhancement",
        "value": "high"
      }
    ],
    "recommendations": [
      "Monitor memory closely during implementation"
    ]
  },
  "timestamp": "2026-01-03T21:23:20.273024+00:00"
}
```

## DIRECTIVE_FORECAST_GLYPH
**Timestamp:** 2026-01-03T21:23:20.273218+00:00

```json
{
  "forecast": {
    "directive_name": "TEST_1",
    "forecast_time": "2026-01-03T21:23:20.273165+00:00",
    "impacts": {
      "memory": "low",
      "matrix": "low",
      "council": "low"
    },
    "confidence": 0.5,
    "risks": [],
    "opportunities": [],
    "recommendations": [
      "Implementation can proceed with standard monitoring"
    ]
  },
  "timestamp": "2026-01-03T21:23:20.273189+00:00"
}
```

## DIRECTIVE_FORECAST_GLYPH
**Timestamp:** 2026-01-03T21:23:20.273341+00:00

```json
{
  "forecast": {
    "directive_name": "TEST_2",
    "forecast_time": "2026-01-03T21:23:20.273302+00:00",
    "impacts": {
      "memory": "low",
      "matrix": "low",
      "council": "low"
    },
    "confidence": 0.5,
    "risks": [],
    "opportunities": [],
    "recommendations": [
      "Implementation can proceed with standard monitoring"
    ]
  },
  "timestamp": "2026-01-03T21:23:20.273319+00:00"
}
```

## COUNCIL_ECHO_GLYPH
**Timestamp:** 2026-01-03T21:23:20.273651+00:00

```json
{
  "deliberation": {
    "topic": "Test topic",
    "timestamp": "2026-01-03T21:23:20.273612+00:00",
    "baseline": {
      "conditions": {
        "practicality": "high",
        "complexity": "medium",
        "risk": "low"
      },
      "votes": {
        "Pragmatist": 1.0217835811977871,
        "Theorist": 0.6981733346714777,
        "Skeptic": 0.3074223033585176,
        "Optimist": 0.4770700329943114,
        "Guardian": 0.621905923763549,
        "Experimentalist": 0.3442076119323644,
        "Error Spotter": 0.6105840525125249
      },
      "consensus": {
        "reached": false,
        "avg_agreement": 0.583,
        "disagreement_level": 0.177,
        "participating_agents": 7
      }
    }
  },
  "timestamp": "2026-01-03T21:23:20.273618+00:00"
}
```

## COUNCIL_ECHO_GLYPH
**Timestamp:** 2026-01-03T21:23:20.273847+00:00

```json
{
  "deliberation": {
    "topic": "Test topic 2",
    "timestamp": "2026-01-03T21:23:20.273794+00:00",
    "baseline": {
      "conditions": {
        "practicality": "low"
      },
      "votes": {
        "Pragmatist": 0.9234295602923522,
        "Theorist": 0.31664931420819986,
        "Skeptic": 0.613035275481767,
        "Optimist": 0.5106704951957429,
        "Guardian": 1.1366213737580158,
        "Experimentalist": 0.7368744354727814,
        "Error Spotter": 0.4343445171235521
      },
      "consensus": {
        "reached": true,
        "avg_agreement": 0.667,
        "disagreement_level": 0.227,
        "participating_agents": 7
      }
    },
    "altered": {
      "conditions": {
        "practicality": "high"
      },
      "votes": {
        "Pragmatist": 0.9259438234539286,
        "Theorist": 0.7250189910114859,
        "Skeptic": 0.7604590917822761,
        "Optimist": 0.8872398482062529,
        "Guardian": 0.4576154555545754,
        "Experimentalist": 0.3002263462495399,
        "Error Spotter": 0.45697802715117836
      },
      "consensus": {
        "reached": true,
        "avg_agreement": 0.645,
        "disagreement_level": 0.206,
        "participating_agents": 7
      }
    },
    "delta": {
      "agreement_change": -0.022,
      "disagreement_change": -0.021,
      "consensus_changed": false
    }
  },
  "timestamp": "2026-01-03T21:23:20.273825+00:00"
}
```

## CHAMBER_CREATED
**Timestamp:** 2026-01-03T21:23:20.279144+00:00

```json
{
  "chamber_id": "integration_test",
  "mode": "test"
}
```

## SIMULATION_COMPLETED
**Timestamp:** 2026-01-03T21:23:20.279248+00:00

```json
{
  "chamber_id": "integration_test",
  "scenario": {
    "protocols": [
      {
        "name": "INTEGRATION_TEST"
      }
    ]
  },
  "started_at": "2026-01-03T21:23:20.279222+00:00",
  "outcomes": [
    {
      "protocol": {
        "name": "INTEGRATION_TEST"
      },
      "test_result": "passed",
      "metrics": {
        "consistency": 0.95,
        "stability": 0.92
      }
    }
  ],
  "completed_at": "2026-01-03T21:23:20.279227+00:00"
}
```

## CHAMBER_CLOSED
**Timestamp:** 2026-01-03T21:23:20.279340+00:00

```json
{
  "chamber_id": "integration_test",
  "results": {
    "chamber_id": "integration_test",
    "mode": "test",
    "active": false,
    "state": {
      "created": "2026-01-03T21:23:20.279099+00:00",
      "agents": [
        {
          "id": "agent_0",
          "name": "Integration Agent",
          "config": {
            "agent_id": "integration_agent",
            "name": "Integration Agent",
            "type": "tester",
            "capabilities": [],
            "mutations": [],
            "performance_history": [],
            "created_at": "2026-01-03T21:23:20.279214+00:00"
          },
          "mutations": [],
          "added_at": "2026-01-03T21:23:20.279219+00:00"
        }
      ],
      "directives": [],
      "glyphs_emitted": [],
      "council_votes": [],
      "reality_drift": 0.0,
      "closed_at": "2026-01-03T21:23:20.279317+00:00"
    }
  }
}
```

## CHAMBER_CREATED
**Timestamp:** 2026-01-03T21:23:20.279730+00:00

```json
{
  "chamber_id": "dup_test",
  "mode": "forecast"
}
```

## CHAMBER_CLOSED
**Timestamp:** 2026-01-03T21:23:20.279849+00:00

```json
{
  "chamber_id": "dup_test",
  "results": {
    "chamber_id": "dup_test",
    "mode": "forecast",
    "active": false,
    "state": {
      "created": "2026-01-03T21:23:20.279667+00:00",
      "agents": [],
      "directives": [],
      "glyphs_emitted": [],
      "council_votes": [],
      "reality_drift": 0.0,
      "closed_at": "2026-01-03T21:23:20.279823+00:00"
    }
  }
}
```

## CHAMBER_CREATED
**Timestamp:** 2026-01-03T21:23:42.428591+00:00

```json
{
  "chamber_id": "test_chamber_1",
  "mode": "forecast"
}
```

## SIMULATION_COMPLETED
**Timestamp:** 2026-01-03T21:23:42.428719+00:00

```json
{
  "chamber_id": "test_chamber_1",
  "scenario": {
    "directives": [
      {
        "name": "TEST_DIRECTIVE"
      }
    ]
  },
  "started_at": "2026-01-03T21:23:42.428673+00:00",
  "outcomes": [
    {
      "directive": {
        "name": "TEST_DIRECTIVE"
      },
      "predicted_impact": {
        "memory_impact": "low",
        "matrix_impact": "medium",
        "council_impact": "high"
      },
      "confidence": 0.75
    }
  ],
  "completed_at": "2026-01-03T21:23:42.428680+00:00"
}
```

## CHAMBER_CLOSED
**Timestamp:** 2026-01-03T21:23:42.428833+00:00

```json
{
  "chamber_id": "test_chamber_1",
  "results": {
    "chamber_id": "test_chamber_1",
    "mode": "forecast",
    "active": false,
    "state": {
      "created": "2026-01-03T21:23:42.428544+00:00",
      "agents": [
        {
          "id": "agent_0",
          "name": "Test Agent",
          "config": {
            "name": "Test Agent",
            "type": "forecaster"
          },
          "mutations": [],
          "added_at": "2026-01-03T21:23:42.428665+00:00"
        }
      ],
      "directives": [
        {
          "directive": {
            "name": "TEST_DIRECTIVE"
          },
          "injected_at": "2026-01-03T21:23:42.428670+00:00",
          "impact": null
        },
        {
          "directive": {
            "name": "TEST_DIRECTIVE"
          },
          "injected_at": "2026-01-03T21:23:42.428677+00:00",
          "impact": null
        }
      ],
      "glyphs_emitted": [],
      "council_votes": [],
      "reality_drift": 0.0,
      "closed_at": "2026-01-03T21:23:42.428809+00:00"
    }
  }
}
```

## DIRECTIVE_FORECAST_GLYPH
**Timestamp:** 2026-01-03T21:23:42.429315+00:00

```json
{
  "forecast": {
    "directive_name": "MEMORY_ENHANCEMENT_DIRECTIVE",
    "forecast_time": "2026-01-03T21:23:42.429271+00:00",
    "impacts": {
      "memory": "high",
      "matrix": "low",
      "council": "low"
    },
    "confidence": 0.85,
    "risks": [
      {
        "area": "memory",
        "risk": "High impact on memory may cause instability",
        "severity": "high"
      }
    ],
    "opportunities": [
      {
        "area": "memory",
        "opportunity": "Potential for memory enhancement",
        "value": "high"
      }
    ],
    "recommendations": [
      "Monitor memory closely during implementation"
    ]
  },
  "timestamp": "2026-01-03T21:23:42.429291+00:00"
}
```

## DIRECTIVE_FORECAST_GLYPH
**Timestamp:** 2026-01-03T21:23:42.429438+00:00

```json
{
  "forecast": {
    "directive_name": "TEST_1",
    "forecast_time": "2026-01-03T21:23:42.429401+00:00",
    "impacts": {
      "memory": "low",
      "matrix": "low",
      "council": "low"
    },
    "confidence": 0.5,
    "risks": [],
    "opportunities": [],
    "recommendations": [
      "Implementation can proceed with standard monitoring"
    ]
  },
  "timestamp": "2026-01-03T21:23:42.429418+00:00"
}
```

## DIRECTIVE_FORECAST_GLYPH
**Timestamp:** 2026-01-03T21:23:42.429542+00:00

```json
{
  "forecast": {
    "directive_name": "TEST_2",
    "forecast_time": "2026-01-03T21:23:42.429500+00:00",
    "impacts": {
      "memory": "low",
      "matrix": "low",
      "council": "low"
    },
    "confidence": 0.5,
    "risks": [],
    "opportunities": [],
    "recommendations": [
      "Implementation can proceed with standard monitoring"
    ]
  },
  "timestamp": "2026-01-03T21:23:42.429513+00:00"
}
```

## COUNCIL_ECHO_GLYPH
**Timestamp:** 2026-01-03T21:23:42.429875+00:00

```json
{
  "deliberation": {
    "topic": "Test topic",
    "timestamp": "2026-01-03T21:23:42.429846+00:00",
    "baseline": {
      "conditions": {
        "practicality": "high",
        "complexity": "medium",
        "risk": "low"
      },
      "votes": {
        "Pragmatist": 1.2,
        "Theorist": 0.43083914110566734,
        "Skeptic": 0.3190588892857881,
        "Optimist": 0.7780975320581667,
        "Guardian": 0.7293910909098046,
        "Experimentalist": 0.4040898510964843,
        "Error Spotter": 0.5509057856053462
      },
      "consensus": {
        "reached": true,
        "avg_agreement": 0.63,
        "disagreement_level": 0.233,
        "participating_agents": 7
      }
    }
  },
  "timestamp": "2026-01-03T21:23:42.429851+00:00"
}
```

## COUNCIL_ECHO_GLYPH
**Timestamp:** 2026-01-03T21:23:42.430040+00:00

```json
{
  "deliberation": {
    "topic": "Test topic 2",
    "timestamp": "2026-01-03T21:23:42.429992+00:00",
    "baseline": {
      "conditions": {
        "practicality": "low"
      },
      "votes": {
        "Pragmatist": 0.748591054533337,
        "Theorist": 0.838929043137695,
        "Skeptic": 0.5523546710155945,
        "Optimist": 0.44361558083697217,
        "Guardian": 1.0418929260871663,
        "Experimentalist": 0.7815782404121283,
        "Error Spotter": 0.47340715463121247
      },
      "consensus": {
        "reached": true,
        "avg_agreement": 0.697,
        "disagreement_level": 0.178,
        "participating_agents": 7
      }
    },
    "altered": {
      "conditions": {
        "practicality": "high"
      },
      "votes": {
        "Pragmatist": 1.1264252243874033,
        "Theorist": 0.4711423120528927,
        "Skeptic": 0.3570280189581756,
        "Optimist": 0.6008954720363033,
        "Guardian": 1.1635388612811832,
        "Experimentalist": 0.5153605821165369,
        "Error Spotter": 0.6565699245123737
      },
      "consensus": {
        "reached": false,
        "avg_agreement": 0.699,
        "disagreement_level": 0.255,
        "participating_agents": 7
      }
    },
    "delta": {
      "agreement_change": 0.002,
      "disagreement_change": 0.077,
      "consensus_changed": true
    }
  },
  "timestamp": "2026-01-03T21:23:42.430020+00:00"
}
```

## CHAMBER_CREATED
**Timestamp:** 2026-01-03T21:23:42.430381+00:00

```json
{
  "chamber_id": "integration_test",
  "mode": "test"
}
```

## SIMULATION_COMPLETED
**Timestamp:** 2026-01-03T21:23:42.430459+00:00

```json
{
  "chamber_id": "integration_test",
  "scenario": {
    "protocols": [
      {
        "name": "INTEGRATION_TEST"
      }
    ]
  },
  "started_at": "2026-01-03T21:23:42.430437+00:00",
  "outcomes": [
    {
      "protocol": {
        "name": "INTEGRATION_TEST"
      },
      "test_result": "passed",
      "metrics": {
        "consistency": 0.95,
        "stability": 0.92
      }
    }
  ],
  "completed_at": "2026-01-03T21:23:42.430441+00:00"
}
```

## CHAMBER_CLOSED
**Timestamp:** 2026-01-03T21:23:42.430539+00:00

```json
{
  "chamber_id": "integration_test",
  "results": {
    "chamber_id": "integration_test",
    "mode": "test",
    "active": false,
    "state": {
      "created": "2026-01-03T21:23:42.430349+00:00",
      "agents": [
        {
          "id": "agent_0",
          "name": "Integration Agent",
          "config": {
            "agent_id": "integration_agent",
            "name": "Integration Agent",
            "type": "tester",
            "capabilities": [],
            "mutations": [],
            "performance_history": [],
            "created_at": "2026-01-03T21:23:42.430429+00:00"
          },
          "mutations": [],
          "added_at": "2026-01-03T21:23:42.430434+00:00"
        }
      ],
      "directives": [],
      "glyphs_emitted": [],
      "council_votes": [],
      "reality_drift": 0.0,
      "closed_at": "2026-01-03T21:23:42.430519+00:00"
    }
  }
}
```

## CHAMBER_CREATED
**Timestamp:** 2026-01-03T21:23:42.430972+00:00

```json
{
  "chamber_id": "dup_test",
  "mode": "forecast"
}
```

## CHAMBER_CLOSED
**Timestamp:** 2026-01-03T21:23:42.431041+00:00

```json
{
  "chamber_id": "dup_test",
  "results": {
    "chamber_id": "dup_test",
    "mode": "forecast",
    "active": false,
    "state": {
      "created": "2026-01-03T21:23:42.430938+00:00",
      "agents": [],
      "directives": [],
      "glyphs_emitted": [],
      "council_votes": [],
      "reality_drift": 0.0,
      "closed_at": "2026-01-03T21:23:42.431020+00:00"
    }
  }
}
```

## CHAMBER_CREATED
**Timestamp:** 2026-01-03T21:23:50.883283+00:00

```json
{
  "chamber_id": "test_chamber_1",
  "mode": "forecast"
}
```

## SIMULATION_COMPLETED
**Timestamp:** 2026-01-03T21:23:50.883394+00:00

```json
{
  "chamber_id": "test_chamber_1",
  "scenario": {
    "directives": [
      {
        "name": "TEST_DIRECTIVE",
        "impact": "analyze"
      }
    ]
  },
  "started_at": "2026-01-03T21:23:50.883363+00:00",
  "outcomes": [
    {
      "directive": {
        "name": "TEST_DIRECTIVE",
        "impact": "analyze"
      },
      "predicted_impact": {
        "memory_impact": "low",
        "matrix_impact": "medium",
        "council_impact": "high"
      },
      "confidence": 0.75
    }
  ],
  "completed_at": "2026-01-03T21:23:50.883372+00:00"
}
```

## CHAMBER_CLOSED
**Timestamp:** 2026-01-03T21:23:50.883539+00:00

```json
{
  "chamber_id": "test_chamber_1",
  "results": {
    "chamber_id": "test_chamber_1",
    "mode": "forecast",
    "active": false,
    "state": {
      "created": "2026-01-03T21:23:50.883238+00:00",
      "agents": [
        {
          "id": "agent_0",
          "name": "Test Agent",
          "config": {
            "name": "Test Agent",
            "type": "forecaster"
          },
          "mutations": [],
          "added_at": "2026-01-03T21:23:50.883357+00:00"
        }
      ],
      "directives": [
        {
          "directive": {
            "name": "TEST_DIRECTIVE",
            "impact": "analyze"
          },
          "injected_at": "2026-01-03T21:23:50.883366+00:00",
          "impact": null
        }
      ],
      "glyphs_emitted": [],
      "council_votes": [],
      "reality_drift": 0.0,
      "closed_at": "2026-01-03T21:23:50.883514+00:00"
    }
  }
}
```
