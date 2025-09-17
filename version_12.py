
import streamlit as st

st.set_page_config(page_title="Sensormatic Digital Dashboard", layout="wide")

st.title("📊 Sensormatic Digital Dashboard")
st.markdown("This dashboard presents performance KPIs and a structured Knowledge Base for content review.")

# ------------------ KPI SECTION ------------------

st.header("🔍 Performance KPIs")

with st.expander("🌐 Site24x7 Uptime & Response"):
    st.metric("Uptime", "99.95%")
    st.metric("Avg Response Time", "320 ms")

with st.expander("🚦 Lighthouse Scores"):
    st.metric("Performance", "85")
    st.metric("Accessibility", "92")
    st.metric("Best Practices", "88")
    st.metric("SEO", "95")

with st.expander("🔍 SEO Metrics"):
    st.metric("Indexed Pages", "1,245")
    st.metric("Broken Links", "3")
    st.metric("Meta Tag Coverage", "98%")

with st.expander("📌 JIRA Tickets"):
    st.metric("Open Bugs", "12")
    st.metric("Resolved This Month", "34")
    st.metric("Avg Resolution Time", "3.2 days")

with st.expander("🔥 Hotjar Insights"):
    st.metric("Avg Scroll Depth", "72%")
    st.metric("Click Rate on CTA", "18%")
    st.metric("Heatmap Coverage", "Top 3 Pages")

# ------------------ KNOWLEDGE BASE SECTION ------------------

st.header("📚 Knowledge Base – Page Type Review & QA")

# Resources
with st.expander("📘 RESOURCES"):
    resources = {
        "Article/Blog": "https://www.sensormatic.com/resources/ar/2025/sustainable-spx-label-blog",
        "Case Study": "https://www.sensormatic.com/resources/cs/2025/nrf-big-show-2025-case-study",
        "TrafficTrak’r": "https://www.sensormatic.com/resources/tt/2025/traffictrakr-202509",
        "Ungated Video": "https://www.sensormatic.com/resources/vi/2025/nrf-2025-big-idea-session-video-recording",
        "Gated Video/Webinar": "https://www.sensormatic.com/resources/vi/2025/orbit-ai-2025-webinar",
        "White Paper": "https://www.sensormatic.com/resources/wp/2025/re-id-revolution-white-paper"
    }
    for name, url in resources.items():
        with st.expander(f"🔹 {name}"):
            st.markdown(f"[View Page]({url})")
            st.subheader("✅ Reviewer Checklist")
            st.markdown("""
            **Content Reviewer**
            - Validate headline, summary, and CTA
            - Check metadata (author, publish date, tags)
            - Ensure internal links and document uploads are correct

            **Language Reviewer**
            - Confirm tone and grammar
            - Validate localization readiness

            **Marketing Stakeholder**
            - Ensure SEO metadata and campaign tracking
            - Confirm CRM/form integration (if gated)
            """)

            st.subheader("🧪 QA Functional Scenarios")
            st.markdown("""
            - Verify page loads without errors
            - Test form submission (if applicable)
            - Check video/document embed functionality
            - Validate redirects and thank-you pages
            - Confirm analytics tracking is firing
            """)

# Media Items
with st.expander("📰 MEDIA ITEMS"):
    media = {
        "In the News": "https://www.sensormatic.com/media-center/in-the-news",
        "Press Release": "https://www.sensormatic.com/media-center"
    }
    for name, url in media.items():
        with st.expander(f"🔹 {name}"):
            st.markdown(f"[View Page]({url})")
            st.subheader("✅ Reviewer Checklist")
            st.markdown("""
            **Content Reviewer**
            - Validate source and quote accuracy
            - Check formatting and attribution

            **Language Reviewer**
            - Confirm clarity and tone
            - Validate localization

            **Marketing Stakeholder**
            - Ensure SEO tagging and social sharing setup
            """)

            st.subheader("🧪 QA Functional Scenarios")
            st.markdown("""
            - Verify page loads and links work
            - Check media embeds (if any)
            - Confirm metadata and schema tags
            """)

# Landing Pages
with st.expander("📍 LANDING PAGES"):
    landing = {
        "Tradeshow LP": None,
        "Campaign Home LP": "https://www.sensormatic.com/landing/source-tagging-registration"
    }
    for name, url in landing.items():
        with st.expander(f"🔹 {name}"):
            if url:
                st.markdown(f"[View Page]({url})")
            else:
                st.markdown("_No URL provided_")
            st.subheader("✅ Reviewer Checklist")
            st.markdown("""
            **Content Reviewer**
            - Validate event/campaign details and CTA
            - Check form setup and thank-you page

            **Language Reviewer**
            - Confirm localization of messaging
            - Validate translation accuracy

            **Marketing Stakeholder**
            - Ensure CRM integration and campaign tracking
            - Confirm lead-gen flow and analytics
            """)

            st.subheader("🧪 QA Functional Scenarios")
            st.markdown("""
            - Test form submission and thank-you redirect
            - Validate UTM parameters and tracking
            - Check responsiveness across devices
            """)

# Solutions
with st.expander("🧩 SOLUTIONS"):
    solutions = {
        "Solution Main Page": "https://www.sensormatic.com/loss-prevention-liability",
        "Solution Sub-page": "https://www.sensormatic.com/loss-prevention-liability/compliance-manager/food-safety"
    }
    for name, url in solutions.items():
        with st.expander(f"🔹 {name}"):
            st.markdown(f"[View Page]({url})")
            st.subheader("✅ Reviewer Checklist")
            st.markdown("""
            **Content Reviewer**
            - Validate solution overview and benefits
            - Check linking to sub-pages and CTAs

            **Language Reviewer**
            - Confirm terminology consistency
            - Validate localization readiness

            **Marketing Stakeholder**
            - Ensure SEO metadata and product alignment
            - Confirm analytics and engagement tracking
            """)

            st.subheader("🧪 QA Functional Scenarios")
            st.markdown("""
            - Verify page loads and links work
            - Test CTA buttons and navigation
            - Confirm analytics and tag firing
            """)

