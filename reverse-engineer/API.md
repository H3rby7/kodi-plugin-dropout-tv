# API

## Endpoints

Optained via Web Console Dev Tools.

Base: `https://api.vhx...`

### watching

#### watching-request

```sh
curl 'https://api.vhx.com/v2/sites/SITE_ID/users/CUSTOMER_ID/watching?per_page=12&include_events=1&include_collections=1' \
  --compressed \
  -H 'User-Agent: Mozilla/5.0 ...' \
  -H 'Accept: application/json' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Referer: https://watch.dropout.tv/' \
  -H 'Authorization: Bearer ey...' \
  -H 'Content-Type: application/json' \
  -H 'X-OTT-Language: en' \
  -H 'Origin: https://watch.dropout.tv' \
  -H 'Sec-GPC: 1' \
  -H 'Connection: keep-alive' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'DNT: 1' \
  -H 'Priority: u=4' \
  -H 'TE: trailers'
```

#### watching-response

```json
{
  "items": [
    {
      "entity": {
        "advertising": {
          "custom_params": {}
        },
        "audio_5_1": false,
        "canonical_collection_id": 1118956,
        "comments_enabled": false,
        "created_at": "2025-08-12T00:06:58.757Z",
        "description": "Brennan Lee Mulligan announces his departure from Dropout and what’s next for him. ",
        "duration": {
          "seconds": 313
        },
        "featured_previews": {
          "16_14": {
            "video_id": null
          },
          "2_3": {
            "video_id": null
          }
        },
        "id": A_VIDEO_ID,
        "is_free": false,
        "live_dvr": false,
        "live_event_id": null,
        "live_status": null,
        "live_unlimited_duration": false,
        "live_video": false,
        "metadata": {
          "advisories": null,
          "cast": null,
          "crew": null,
          "genres": null,
          "ratings": null,
          "release_dates": [
            {
              "date": "2025-08-15",
              "location": "US"
            }
          ],
          "tags": [
            "the real ending"
          ],
          "custom": [],
          "movie": null,
          "season": {
            "episode_number": null,
            "name": "Season 7",
            "number": 7
          },
          "series": {
            "name": "Game Changer",
            "id": "121093"
          }
        },
        "page_url": "https://watch.dropout.tv/game-changer/season:7/videos/brennan-s-exit-extended-cut",
        "playback_features": [],
        "product_ids": [
          A_PRODUCT_ID,
          A_PRODUCT_ID,
          ANOTHER_PRODUCT_ID
        ],
        "scheduled_at": null,
        "short_description": "Brennan Lee Mulligan announces his departure from Dropout and what’s next for him. ",
        "site_id": SITE_ID,
        "slug": "brennan-s-exit-extended-cut",
        "thumbnails": {
          "16_9": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "1_1": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "2_3": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "2_3_featured": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "16_6": null,
          "16_14": null
        },
        "title": "Brennan's Exit (Extended Cut)",
        "trailer": false,
        "type": "video",
        "up_next_offset_seconds": 0,
        "updated_at": "2025-11-16T09:51:02.429Z",
        "thumbnail_badges": []
      },
      "entity_id": A_VIDEO_ID,
      "entity_type": "video",
      "continue_watching": {
        "description": "Up next in Game Changer",
        "movie": null,
        "playlist": null,
        "season": {
          "id": 1118956,
          "number": 7
        },
        "series": {
          "id": 121093
        }
      }
    }
  ],
  "pagination": {
    "count": 1,
    "current": 1,
    "page": 1,
    "per_page": 12,
    "template_url": "https://api.vhx.com/v2/sites/SITE_ID/users/CUSTOMER_ID/watching?page={page}\u0026per_page={per_page}"
  }
}
```

### watchlist

#### watchlist-request

```sh
curl 'https://api.vhx.tv/customers/CUSTOMER_ID/watchlist?product=ANOTHER_PRODUCT_ID&collection=https://api.vhx.tv/customers/CUSTOMER_ID/watchlist&per_page=12&include_products=true' \
  --compressed \
  -H 'User-Agent: Mozilla/5.0 ...' \
  -H 'Accept: application/json' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Referer: https://watch.dropout.tv/' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ey...' \
  -H 'X-OTT-Language: en' \
  -H 'Origin: https://watch.dropout.tv' \
  -H 'Sec-Fetch-Storage-Access: none' \
  -H 'Sec-GPC: 1' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: __cf_bm=**************-1.0.1.1-********************; _cfuvid=********************-0.0.1.1-604800000' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'DNT: 1' \
  -H 'Priority: u=4' \
  -H 'TE: trailers'
```

#### watchlist-response

```json
{
  "_links": {
    "self": {
      "href": "https://api.vhx.tv/customers/CUSTOMER_ID/watchlist?page=1\u0026per_page=12"
    },
    "first": {
      "href": "https://api.vhx.tv/customers/CUSTOMER_ID/watchlist?page=1\u0026per_page=12"
    },
    "prev": {
      "href": null
    },
    "next": {
      "href": null
    },
    "last": {
      "href": "https://api.vhx.tv/customers/CUSTOMER_ID/watchlist?"
    }
  },
  "count": 1,
  "total": 1,
  "_embedded": {
    "items": [
      {
        "_links": {
          "self": {
            "href": "https://api.vhx.tv/collections/POSSIBLY_A_COLLECTION_ID"
          },
          "items": {
            "href": "https://api.vhx.tv/collections/POSSIBLY_A_COLLECTION_ID/items"
          },
          "collection_page": {
            "href": "https://watch.dropout.tv/dimension-20-mentopolis"
          },
          "seasons": {
            "href": "https://api.vhx.tv/collections/POSSIBLY_A_COLLECTION_ID/items"
          }
        },
        "id": POSSIBLY_A_COLLECTION_ID,
        "name": "Dimension 20: Mentopolis",
        "title": "Dimension 20: Mentopolis",
        "description": "Welcome to Mentopolis - the city that exists only in your mind.",
        "short_description": "Welcome to Mentopolis - the city that exists only in your mind.",
        "slug": "dimension-20-mentopolis",
        "thumbnail": {
          "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
        },
        "type": "series",
        "seasons_count": 1,
        "items_count": 1,
        "files_count": 0,
        "live_events_count": 0,
        "created_at": "2023-07-21T19:31:46Z",
        "updated_at": "2024-03-22T00:39:26Z",
        "has_free_videos": false,
        "is_available": true,
        "geo_available": "",
        "geo_unavailable": "",
        "metadata": {},
        "plans": [
          "standard"
        ],
        "is_featured": false,
        "featured_category_thumbnail_layout": null,
        "overlay_configuration": {},
        "is_automatic": false,
        "additional_images": {
          "aspect_ratio_1_1": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "aspect_ratio_2_3": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "aspect_ratio_2_3_featured": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "aspect_ratio_12_5_logo": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "aspect_ratio_16_6": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "aspect_ratio_16_14": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "aspect_ratio_16_9_background": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          }
        },
        "thumbnail_badges": [],
        "thumbnail_size": null,
        "hide_item_title": false,
        "has_only_free_videos": false,
        "has_any_free_videos": false,
        "has_only_public_videos": false,
        "item_id": 175356801,
        "tags": null
      }
    ]
  }
}
```

### items

#### items-request

```sh
curl 'https://api.vhx.com/v2/sites/SITE_ID/collections/COLLECTION_ID/items?include_products_for=web&per_page=12&include_events=1' \
  --compressed \
  -H 'User-Agent: Mozilla/5.0 ...' \
  -H 'Accept: application/json' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Referer: https://watch.dropout.tv/' \
  -H 'Authorization: Bearer ey...' \
  -H 'Content-Type: application/json' \
  -H 'X-OTT-Language: en' \
  -H 'Origin: https://watch.dropout.tv' \
  -H 'Sec-GPC: 1' \
  -H 'Connection: keep-alive' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'DNT: 1' \
  -H 'Priority: u=4' \
  -H 'TE: trailers'
```

#### items-response

```json
{
  "items": [
    {
      "created_at": "2026-02-18T19:52:44.709Z",
      "entity": {
        "canonical_collection_id": null,
        "comments_enabled": false,
        "created_at": "2026-02-10T00:17:49.273Z",
        "description": "An always-on channel featuring your favorite Dropout content, ad-free.\n\nFAQ here: https://www.dropout.tv/24-7-faq",
        "id": 48686,
        "include_live_engagement": false,
        "is_free": false,
        "latest_video": {
          "id": 3946713,
          "live_status": "started",
          "scheduled_at": null
        },
        "live_engagement_registration_required": true,
        "metadata": {
          "advisories": null,
          "cast": null,
          "crew": null,
          "genres": null,
          "ratings": null,
          "tags": null,
          "custom": []
        },
        "page_url": "https://watch.dropout.tv/events/dropout-24-7",
        "product_ids": [
          A_PRODUCT_ID,
          ANOTHER_PRODUCT_ID
        ],
        "short_description": "An always-on channel featuring your favorite Dropout content, ad-free.",
        "slug": "dropout-24-7",
        "thumbnails": {
          "16_9": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "1_1": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "2_3": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "2_3_featured": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "16_6": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "16_14": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          }
        },
        "title": "Dropout 24/7",
        "type": "live_event",
        "updated_at": "2026-02-18T03:39:53.429Z"
      },
      "entity_id": 48686,
      "entity_type": "live_event",
      "id": 263391211,
      "position": 1,
      "updated_at": "2026-02-18T19:52:50.701Z"
    },
    {
      "created_at": "2026-03-05T22:56:52.023Z",
      "entity": {
        "advertising": {
          "custom_params": {}
        },
        "audio_5_1": false,
        "canonical_collection_id": 1462684,
        "comments_enabled": false,
        "created_at": "2026-03-05T22:56:19.267Z",
        "description": "The crew of Very Important People discuss how Frankie Quiñones became Lil Huffy.",
        "duration": {
          "seconds": 340
        },
        "featured_previews": {
          "16_14": {
            "video_id": null
          },
          "2_3": {
            "video_id": null
          }
        },
        "id": 3966433,
        "is_free": false,
        "live_dvr": false,
        "live_event_id": null,
        "live_status": null,
        "live_unlimited_duration": false,
        "live_video": false,
        "metadata": {
          "advisories": null,
          "cast": null,
          "crew": null,
          "genres": null,
          "ratings": null,
          "release_dates": [
            {
              "date": "2026-03-13",
              "location": null
            }
          ],
          "tags": [
            "Very Important People",
            "vic michaelis",
            "disguises",
            "makeup",
            "makeovers",
            "interviews",
            "improv",
            "surprises",
            "frankie quiñones",
            "tamar levine",
            "alex perrone",
            "bruce spaulding fuller",
            "alisha silverstein",
            "paul robalino",
            "behind the scenes"
          ],
          "custom": [],
          "movie": null,
          "season": {
            "episode_number": null,
            "name": "Season 3",
            "number": 3
          },
          "series": {
            "name": "Very Important People",
            "id": "955941"
          }
        },
        "page_url": "https://watch.dropout.tv/videos/last-looks-lil-huffy",
        "playback_features": [],
        "product_ids": [
          A_PRODUCT_ID,
          A_PRODUCT_ID,
          ANOTHER_PRODUCT_ID
        ],
        "scheduled_at": null,
        "short_description": "The crew of Very Important People discuss how Frankie Quiñones became Lil Huffy.",
        "site_id": SITE_ID,
        "slug": "last-looks-lil-huffy",
        "thumbnails": {
          "16_9": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "1_1": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "2_3": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "2_3_featured": {
            "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
          },
          "16_6": null,
          "16_14": null
        },
        "title": "Last Looks: Lil Huffy",
        "trailer": false,
        "type": "video",
        "up_next_offset_seconds": 0,
        "updated_at": "2026-03-13T17:30:01.316Z",
        "thumbnail_badges": []
      },
      "entity_id": 3966433,
      "entity_type": "video",
      "id": 274629451,
      "position": 2,
      "updated_at": "2026-03-13T17:30:00.878Z"
    }
  ],
  "pagination": {
    "count": 22,
    "current": 12,
    "page": 1,
    "per_page": 12,
    "template_url": "https://api.vhx.com/v2/sites/SITE_ID/collections/COLLECTION_ID/items?page={page}\u0026per_page={per_page}"
  }
}
```

### featured_items

#### featured_items-request

```sh
curl 'https://api.vhx.tv/products/featured_items?site_id=SITE_ID&hub_id=HUB_ID' \
  --compressed \
  -H 'User-Agent: Mozilla/5.0 ...' \
  -H 'Accept: application/json' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Referer: https://watch.dropout.tv/' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ey...' \
  -H 'X-OTT-Language: en' \
  -H 'Origin: https://watch.dropout.tv' \
  -H 'Sec-Fetch-Storage-Access: none' \
  -H 'Sec-GPC: 1' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: __cf_bm=**************-1.0.1.1-********************; _cfuvid=********************-0.0.1.1-604800000' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'DNT: 1' \
  -H 'Priority: u=4' \
  -H 'TE: trailers'
```

#### featured_items-response

```json
{
  "_links": {
    "self": {
      "href": "https://api.vhx.tv/products/featured_items?site=SITE_ID\u0026page=1\u0026per_page=50"
    },
    "first": {
      "href": "https://api.vhx.tv/products/featured_items?site=SITE_ID\u0026page=1\u0026per_page=50"
    },
    "prev": {
      "href": null
    },
    "next": {
      "href": null
    },
    "last": {
      "href": "https://api.vhx.tv/products/featured_items?site=SITE_ID\u0026"
    }
  },
  "count": 11,
  "total": 11,
  "_embedded": {
    "items": [
      {
        "_links": {
          "collection_page": {
            "href": "https://watch.dropout.tv/very-important-people"
          }
        },
        "additional_images": {
          "aspect_ratio_12_5_logo": {
            "source": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/..."
          },
          "aspect_ratio_16_6": {
            "source": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/..."
          },
          "aspect_ratio_16_14": {
            "source": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/..."
          },
          "aspect_ratio_16_9_background": {
            "source": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/..."
          }
        },
        "created_at": "2023-11-22T21:49:58Z",
        "description": "Comedians are given makeovers to be transformed into someone completely new, and then have a fully-improvised interview with host Vic Michaelis. New episodes every other Thursday.",
        "id": 955941,
        "name": "Very Important People",
        "short_description": "Vic Michaelis interviews society's most interesting characters.",
        "slug": "very-important-people",
        "thumbnail": {
          "blurred": "https://vhx.imgix.net/...",
            "large": "https://vhx.imgix.net/...",
            "medium": "https://vhx.imgix.net/...",
            "small": "https://vhx.imgix.net/...",
            "source": "https://vhx.imgix.net/..."
        },
        "trailer_url": "https://watch.dropout.tv/videos/very-important-people-season-3-trailer",
        "type": "series",
        "updated_at": "2026-01-12T18:20:32Z",
        "seasons_count": 3
      }
    ]
  }
}
```


### play_state

#### play_state-request

```sh
curl 'https://api.vhx.com/v2/sites/SITE_ID/users/CUSTOMER_ID/play_state?video_ids=A_VIDEO_ID,ANOTHER_VIDEO_ID,...' \
  --compressed \
  -H 'User-Agent: Mozilla/5.0 ...' \
  -H 'Accept: application/json' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Referer: https://watch.dropout.tv/' \
  -H 'Authorization: Bearer ey...' \
  -H 'Content-Type: application/json' \
  -H 'X-OTT-Language: en' \
  -H 'Origin: https://watch.dropout.tv' \
  -H 'Sec-GPC: 1' \
  -H 'Connection: keep-alive' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'DNT: 1' \
  -H 'Priority: u=4'
```

#### play_state-response

```json
{
  "entries": []
}
```