using System;
using System.Reflection;
using Terraria;
using TerrariaApi.Server;
using TShockAPI;
using TShockAPI.DB;
using Newtonsoft.Json;
using Rests;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;

namespace cTerrachar
{
    public struct DBItem
    {
        public int PieceID;
        public int Slot;
    }
    public class RelevantInfo
    {
        public string Name { get; set; }
        public int ID { get; set; }

        public int Hair { get; set; }
        public int SkinVariant;

        public int[] HairColor;
        public int[] SkinColor;
        public int[] EyeColor;
        public int[] ShirtColor;
        public int[] UnderShirtColor;
        public int[] PantsColor;
        public int[] ShoeColor;

        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? HeadSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? BodySlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? LegsSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? HandsOnSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? HandsOffSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? BackSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? FrontSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? ShoeSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? WaistSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? WingSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? ShieldSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? NeckSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? FaceSlot;
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? BalloonSlot;

        public static RelevantInfo GetRelevance(Player player)
        {
            RelevantInfo relevantPlr = new RelevantInfo();
            relevantPlr.EyeColor = new int[] { player.eyeColor.R, player.eyeColor.G, player.eyeColor.B };
            relevantPlr.HairColor = new int[] { player.hairColor.R, player.hairColor.G, player.hairColor.B };
            relevantPlr.PantsColor = new int[] { player.pantsColor.R, player.pantsColor.G, player.pantsColor.B };
            relevantPlr.ShirtColor = new int[] { player.shirtColor.R, player.shirtColor.G, player.shirtColor.B };
            relevantPlr.ShoeColor = new int[] { player.shoeColor.R, player.shoeColor.G, player.shoeColor.B };
            relevantPlr.SkinColor = new int[] { player.skinColor.R, player.skinColor.G, player.skinColor.B };
            relevantPlr.UnderShirtColor = new int[] { player.underShirtColor.R, player.underShirtColor.G, player.underShirtColor.B };
            relevantPlr.SkinVariant = player.skinVariant;
            relevantPlr.Hair = player.hair;
            relevantPlr.HeadSlot = player.head < 1 ? (int?)null : player.head;
            relevantPlr.BodySlot = player.body < 1 ? (int?)null : player.body;
            relevantPlr.LegsSlot = player.legs < 1 ? (int?)null : player.legs;
            relevantPlr.HandsOnSlot = player.handon < 1 ? (int?)null : player.handon;
            relevantPlr.HandsOffSlot = player.handoff < 1 ? (int?)null : player.handoff;
            relevantPlr.BackSlot = player.back < 1 ? (int?)null : player.head;
            relevantPlr.FrontSlot = player.front < 1 ? (int?)null : player.front;
            relevantPlr.ShoeSlot = player.shoe < 1 ? (int?)null : player.shoe;
            relevantPlr.WaistSlot = player.waist < 1 ? (int?)null : player.waist;
            relevantPlr.WingSlot = player.wings < 1 ? (int?)null : player.wings;
            relevantPlr.ShieldSlot = player.shield < 1 ? (int?)null : player.shield;
            relevantPlr.NeckSlot = player.neck < 1 ? (int?)null : player.neck;
            relevantPlr.FaceSlot = player.face < 1 ? (int?)null : player.face;
            relevantPlr.BalloonSlot = player.balloon < 1 ? (int?)null : player.balloon;

            relevantPlr.Name = player.name;
            return relevantPlr;
        }

        public static RelevantInfo GetRelevance(QueryResult reader)
        {

            bool[] hiddens = new bool[20];
            RelevantInfo relevantPlr = new RelevantInfo();
            Color eyeColor = (Color)TShock.Utils.DecodeColor(reader.Get<Int32>("eyecolor"));
            Color hairColor = (Color)TShock.Utils.DecodeColor(reader.Get<Int32>("haircolor"));
            Color pantsColor = (Color)TShock.Utils.DecodeColor(reader.Get<Int32>("pantscolor"));
            Color shirtColor = (Color)TShock.Utils.DecodeColor(reader.Get<Int32>("shirtcolor"));
            Color shoeColor = (Color)TShock.Utils.DecodeColor(reader.Get<Int32>("shoecolor"));
            Color skinColor = (Color)TShock.Utils.DecodeColor(reader.Get<Int32>("skincolor"));
            Color underShirtColor = (Color)TShock.Utils.DecodeColor(reader.Get<Int32>("undershirtcolor"));
            relevantPlr.EyeColor = new int[] { eyeColor.R, eyeColor.G, eyeColor.B };
            relevantPlr.HairColor = new int[] { hairColor.R, hairColor.G, hairColor.B };
            relevantPlr.PantsColor = new int[] { pantsColor.R, pantsColor.G, pantsColor.B };
            relevantPlr.ShirtColor = new int[] { shirtColor.R, shirtColor.G, shirtColor.B };
            relevantPlr.ShoeColor = new int[] { shoeColor.R, shoeColor.G, shoeColor.B };
            relevantPlr.SkinColor = new int[] { skinColor.R, skinColor.G, skinColor.B };
            relevantPlr.UnderShirtColor = new int[] { underShirtColor.R, underShirtColor.G, underShirtColor.B };
            relevantPlr.SkinVariant = reader.Get<Int32>("skinvariant");
            relevantPlr.Hair = reader.Get<Int32>("hair");

            for (int i = 0; i < 20; i++)
                if (i < 10)
                    hiddens[i] = (reader.Get<Int32>("hideVisuals") & 1 << i) != 0;
                else
                    hiddens[i] = false;

            string[] inventory_entries = reader.Get<String>("inventory").Split('~');
            NetItem parsed;
            Item item;
            // Because vanity items are stored after regular, if one is wearing vanity it will replace the former
            int not_weird = 0;
            for (int i = 59; i < 79; i++)
            {
                not_weird = i - 59;
                parsed = NetItem.Parse(inventory_entries[i]);
                if (parsed.NetId < 1)
                    continue;
                item = new Item();
                item.SetDefaults(parsed.NetId);
                // Head
                if ((i == 59 || i == 69) && item.headSlot >= 0)
                    relevantPlr.HeadSlot = (item.headSlot == 0) ? (int?)null : item.headSlot;
                // Body
                else if ((i == 60 || i == 70) && item.bodySlot >= 0)
                    relevantPlr.BodySlot = (item.bodySlot == 0) ? (int?)null : item.bodySlot;
                // Legs
                else if ((i == 61 || i == 71) && item.legSlot >= 0)
                    relevantPlr.LegsSlot = (item.legSlot == 0) ? (int?)null : item.legSlot;
                // Accessories
                else if (((i >= 62 && i <= 67) && !hiddens[not_weird]) || i >= 72 && i <= 77)
                {
                    if (item.handOnSlot >= 0)
                        relevantPlr.HandsOnSlot = item.handOnSlot;
                   if (item.handOffSlot >= 0)
                        relevantPlr.HandsOffSlot = item.handOffSlot;


                    if (item.backSlot >= 0)
                    {
                        relevantPlr.BackSlot = item.backSlot;
                        relevantPlr.FrontSlot = null;
                    }
                    if (item.frontSlot > 0)
                        relevantPlr.FrontSlot = item.frontSlot;
                    if (item.shoeSlot > 0)
                        relevantPlr.ShoeSlot = item.shoeSlot;
                    if (item.waistSlot > 0)
                        relevantPlr.WaistSlot = item.waistSlot;
                    if (item.wingSlot > 0)
                        relevantPlr.WingSlot = item.wingSlot;
                    if (item.shieldSlot > 0)
                        relevantPlr.ShieldSlot = item.shieldSlot;
                    if (item.neckSlot > 0)
                        relevantPlr.NeckSlot = item.neckSlot;
                    if (item.faceSlot > 0)
                        relevantPlr.FaceSlot = item.faceSlot;
                    if (item.balloonSlot > 0)
                        relevantPlr.BalloonSlot = item.balloonSlot;
                }
            }


            // Robes and set pieces that stretch
            bool wearsRobe = false;
            int news = Player.SetMatch(1, relevantPlr.BodySlot.HasValue ? relevantPlr.BodySlot.Value : 0, Terraria.ID.PlayerVariantID.Sets.Male[relevantPlr.SkinVariant], ref wearsRobe);
            if (news != -1)
                relevantPlr.LegsSlot = news;
            news = Player.SetMatch(2, relevantPlr.LegsSlot.HasValue ? relevantPlr.LegsSlot.Value : 0, Terraria.ID.PlayerVariantID.Sets.Male[relevantPlr.SkinVariant], ref wearsRobe);
            if (news != -1)
                relevantPlr.LegsSlot = news;
            news = Player.SetMatch(0, relevantPlr.HeadSlot.HasValue ? relevantPlr.HeadSlot.Value : 0, Terraria.ID.PlayerVariantID.Sets.Male[relevantPlr.SkinVariant], ref wearsRobe);
            if (news != -1)
                relevantPlr.HeadSlot = news;

            // Conditionals
            if (relevantPlr.WingSlot.HasValue)
            {
                relevantPlr.BackSlot = null;
                relevantPlr.FrontSlot = null;
            }

            if (relevantPlr.HeadSlot.HasValue && relevantPlr.HeadSlot != 0)
            {
                relevantPlr.FaceSlot = relevantPlr.FaceSlot.HasValue ? ((relevantPlr.FaceSlot == 7) ? 7 : (int?)null) : (int?)null;
            }

            return relevantPlr;
        }

    }
    [ApiVersion(2, 0)]
    public class cTerrachar : TerrariaPlugin
    {
        public override string Author => "Shoot";
        public override string Description => "Generate player avatars";
        public override string Name => "cTerrachar";
        public override Version Version => Assembly.GetExecutingAssembly().GetName().Version;


        public cTerrachar(Main game)
            : base(game)
        {
            Order = 10;
        }

        public override void Initialize()
        {
            TShock.RestApi.Register(new RestCommand("/cterrachar/active_players", getPlayers));
            TShock.RestApi.Register(new RestCommand("/cterrachar/player", getPlayer));
        }

        private object getPlayer(RestRequestArgs args)
        {
            string strName = args.Parameters["name"];
            if (string.IsNullOrEmpty(strName))
                return new RestObject()
                {
                    { "error" , "expected player name in 'name'" }
                };

            User usr = TShock.Users.GetUserByName(strName);
            if (usr == null)
                return new RestObject()
                {
                    { "error", "player not found" }
                };
            List<TSPlayer> plrs = TShock.Utils.FindPlayer(strName);
            // Player is online, no need to fetch from DB
            if (plrs.Count == 1)
                return new RestObject() { { "player", RelevantInfo.GetRelevance(plrs[0].TPlayer) } };
            try
            {
                // Fetch from DB
                using (var reader = TShock.DB.QueryReader("SELECT * FROM tsCharacter where account =@0", usr.ID))
                {
                    if (reader.Read())
                    {
                        RelevantInfo plr;
                        foreach (var player in TShock.Players.Where(p => null != p && p.User.Name == usr.Name))
                        {
                            // Some reason we didn't get the idea, lets use the real player if they're online
                            plr = RelevantInfo.GetRelevance(player.TPlayer);
                            plr.Name = usr.Name;
                            plr.ID = usr.ID;
                            return new RestObject() { { "player", plr } };
                        }
                        // Load from DB
                        plr = RelevantInfo.GetRelevance(reader);
                        plr.Name = usr.Name;
                        plr.ID = usr.ID;
                        return new RestObject() { { "player", plr } };
                    }
                }
            }
            catch (Exception ex)
            {
                return new RestObject() { { "error", ex.Message } };
            }
            return new RestObject()
                {
                    { "error", "player not found" }
                };
        }

        private object getPlayers(RestRequestArgs args)
        {
            List<RelevantInfo> relevantPlayers = new List<RelevantInfo>();
            for (int i = 0; i < Main.player.Length; i++)
            {
                Player player = Main.player[i];
                if (!String.IsNullOrEmpty(player?.name))
                {
                    relevantPlayers.Add(RelevantInfo.GetRelevance(player));
                }
            }
            return new RestObject()
            {
                { "count", relevantPlayers.Count },
                { "players", relevantPlayers}
            };
        }


    }
}
